import requests
import json

class GetPrograms:
    def __init__(self, url):
        self.url = url

    def get_programs(self):
        response = requests.get(self.url)
        return response.content

    def program_agencies(self):
        programs_list = []
        response_content = self.get_programs()
        try:
            programs = json.loads(response_content)
            print(f"Type of programs: {type(programs)}") # Debugging line
            print(f"Content of programs: {programs}") # Debugging line
            for program in programs:
                programs_list.append(program["agency"])
        except json.JSONDecodeError:
            print("Error: Response content is not valid JSON.")
            print(response_content)
        return programs_list

if __name__ == "__main__":
    url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    programs = GetPrograms(url)
    agencies = programs.program_agencies()
    for agency in set(agencies):
        print(agency)
