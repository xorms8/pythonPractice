
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

result = []
def set_contact():
    name = input('이름은? ')
    phone_number = input('전화번호는? ')
    email = input('이메일은? ')
    addr = input('주소는? ')
    result.append(name)
    result.append(phone_number)
    result.append(email)
    result.append(addr)
    return
    pass

def print_contact(contact_list):
    print('이름: {}'.format(result[0]))
    print('전화번호: {}'.format(result[1]))
    print('이메일: {}'.format(result[2]))
    print('주소: {}'.format(result[3]))
    pass

def delete_contact(name):
    # 여기에 코드 작성
    input("삭제할 이름은?",name)
    if name == result[0]:
        result.remove(result)
    pass

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    run()