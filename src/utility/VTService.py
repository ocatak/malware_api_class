import requests
import time


class VTService:

    def rescan_virus(self, resource, api_key):
        params = {'apikey': api_key, 'input': resource}

        response = requests.post('https://www.virustotal.com/vtapi/v2/file/rescan',
                                 params=params)
        json_response = response.json()
        print(json_response)
        return json_response

    def report_virus(self, resource, api_key):

        params = {'apikey': api_key, 'resource': resource}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip,  My Python requests library example client or username"
        }
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                params=params, headers=headers)
        json_response = response.json()
        # print(json_response)
        return json_response


    def ask_to_virus_total_service(self, resource, api_key):
        try:
            return self.report_virus(resource, api_key)
        except Exception as e:
            print("ask_to_virus_total_service..." + str(e))
            time.sleep(3)
            return self.ask_to_virus_total_service(resource, api_key)

    def fetch_engine_values(self, resource, api_key):
        result_str = resource + ":"
        response = self.ask_to_virus_total_service(resource, api_key)
        scans = response.get("scans")

        for engine in scans:
            engine_info = scans.get(engine)
            if engine_info.get("detected") is True:
                tmp_str = str(engine_info.get("result"))
                result_str = result_str + engine + "_" + tmp_str + ","

        return result_str
