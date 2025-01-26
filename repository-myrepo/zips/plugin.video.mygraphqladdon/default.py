import sys
import xbmc
import xbmcgui
import xbmcplugin
import requests

def send_to_graphql_api(file_path):
    query = '''
    query ProcessVideo($filePath: String!) {
        processVideo(filePath: $filePath)
    }
    '''
    endpoint = "https://192.168.0.100:8080/api/graphql"
    try:
        response = requests.post(
            endpoint,
            json={"query": query, "variables": {"filePath": file_path}}
        )
        result = response.json()
        if result.get("data", {}).get("processVideo", {}):
            xbmcgui.Dialog().notification(
                "GraphQL Addon",
                f"Successfully processed: {file_path}",
                xbmcgui.NOTIFICATION_INFO
            )
        else:
            xbmcgui.Dialog().notification(
                "GraphQL Addon",
                f"Failed to process: {file_path}",
                xbmcgui.NOTIFICATION_ERROR
            )
    except Exception as e:
        xbmcgui.Dialog().notification(
            "GraphQL Addon",
            f"Error: {str(e)}",
            xbmcgui.NOTIFICATION_ERROR
        )

def refresh_file_manager():
    xbmc.executebuiltin('Container.Refresh')

def main():
    file_path = xbmc.getInfoLabel('ListItem.FileNameAndPath')
    if file_path:
        send_to_graphql_api(file_path)
        refresh_file_manager()
    else:
        xbmcgui.Dialog().notification(
            "GraphQL Addon",
            "No file selected",
            xbmcgui.NOTIFICATION_WARNING
        )

if __name__ == "__main__":
    main()
