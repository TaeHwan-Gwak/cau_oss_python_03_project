from file_manager import read_file
import parking_spot_manager

def start_process(path):
    str_list = read_file(path)
    parking_spot_list = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            # version#2 에 해당하는 내용으로써 print_spot 함수를 호출한다.
            parking_spot_manager.print_spots(parking_spot_list)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            # version#3 에 해당하는 내용으로써 각각의 경우에 맞는 filter_by_(key) 함수를 호출한다.
            if select == 1:
                keyword = input('type name:')
                parking_spot_list = parking_spot_manager.filter_by_name(parking_spot_list, keyword)
            elif select == 2:
                keyword = input('type city:')
                parking_spot_list = parking_spot_manager.filter_by_city(parking_spot_list, keyword)
            elif select == 3:
                keyword = input('type district:')
                parking_spot_list = parking_spot_manager.filter_by_district(parking_spot_list, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                parking_spot_list = parking_spot_manager.filter_by_ptype(parking_spot_list, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_long = float(input('type min long:'))  # parking_spot_list 와 동일하게 하기 위해 min_lon 을 min_long 으로 변경
                max_long = float(input('type max long:'))  # 위와 동일
                parking_spot_list = parking_spot_manager.filter_by_location(parking_spot_list,
                                                                            (min_lat, max_lat, min_long, max_long))
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                # 입력한 keyword에 맞게 sort_by_keyword 함수를 호출하여 실행.
                parking_spot_list = parking_spot_manager.sort_by_keyword(parking_spot_list, keyword)
            else:
                print("invalid input")
        elif select == 4:
            # version#2 에 해당하는 내용으로써 Exit를 출력하고 반복을 종료하도록 한다.
            print("Exit")
            break
        else:
            print("invalid input")
