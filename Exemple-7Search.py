from ast import Continue
import os
import time
from colorama import Fore

os.system("title 7Search By Law")

user = os.getenv("USERNAME")

try:
    folder_database_relative = "./DB7SEARCH"
    folder_database = os.path.abspath(folder_database_relative)

    search = input(f'''{Fore.LIGHTMAGENTA_EX}
███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
╚════██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
    ██╔╝███████╗█████╗  ███████║██████╔╝██║     ███████║  
   ██╔╝ ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
   ██║  ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
   ╚═╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                     User@{user}
Search -> {Fore.GREEN}''')

    print(f"{Fore.LIGHTMAGENTA_EX}Search Please Wait...")

    try:
        files_searched = 0

        def check(folder):
            global files_searched
            results_found = False
            print(f'''{Fore.LIGHTMAGENTA_EX}Search in {Fore.GREEN} {folder}

''')
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, 'r', encoding='utf-8') as file:
                            line_number = 0
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{search}")
                                    print(f"""{Fore.GREEN}
/Folder : {folder}
/File   : {element}
/Line   : {line_number}
/Result : {line_info}
    """)
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, 'r', encoding='latin-1') as file:
                                files_searched += 1
                                line_number = 0
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(search, f"{search}")
                                        print(f"""{Fore.GREEN}
/Folder : {folder}
/File   : {element}
/Line   : {line_number}
/Result : {line_info}
    """)
                        except Exception as e:
                            print(f"{Fore.RED}Error reading file")
                            time.sleep(3)
                    except Exception as e:
                        print(f"{Fore.RED}Error reading file")
                        time.sleep(3)
            return results_found
        

        results_found = check(folder_database)
        if not results_found:
            print(f"{Fore.RED}No result found")
            time.sleep(3)

    except Exception as e:
        print(f"{Fore.RED}Error during search")
        time.sleep(3)

    Continue()
except Exception as e:
    print(f'{Fore.RED}Error Db...')
    time.sleep(3)
    
