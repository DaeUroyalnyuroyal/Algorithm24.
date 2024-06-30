import tkinter as tk
from tkinter import messagebox

# 로그인창
def show_login():
    login_frame.pack(pady=20)        # 로그인창 보이기
    register_frame.pack_forget()     # 회원가입창 숨기기

# 회원가입창
def show_register():
    register_frame.pack(pady=20)     # 회원가입창 보이기
    login_frame.pack_forget()        # 로그인창 숨기기

# 사용자 선택 시 로그인 및 회원가입 버튼 표시
def show_user_options():
    main_select_frame.pack_forget()  # 사용자/관리자 선택창 숨기기
    user_select_frame.pack(pady=20)  # 로그인/회원가입 버튼 보이기

# 로그인 함수
def user_login():
    username = user_login_entry.get()  # 사용자 이름 입력값 가져오기
    password = user_login_password_entry.get()  # 비밀번호 입력값 가져오기

    # 파일에서 아이디와 비밀번호 확인
    try:
        with open("C:/Users/User/Algorithm245/창업프로젝트1/users.txt", "r") as file:
            for line in file:
                try:
                    stored_username, stored_password, _, _ = line.strip().split(',')  # 파일에서 저장된 아이디와 비밀번호 읽기
                except ValueError:
                    continue
                if username == stored_username and password == stored_password:  # 입력된 아이디와 비밀번호가 일치하는지 확인
                    messagebox.showinfo("로그인 성공", "로그인에 성공했습니다.")  # 로그인 성공 메시지
                    return
            messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 잘못되었습니다.")  # 로그인 실패 메시지
    except FileNotFoundError:
        messagebox.showerror("로그인 실패", "사용자 정보 파일을 찾을 수 없습니다.")

# 회원가입 함수
def register():
    name = register_name_entry.get()  # 입력된 이름을 가져옴
    username = register_username_entry.get()  # 입력된 사용자 이름을 가져옴
    password = register_password_entry.get()  # 입력된 비밀번호를 가져옴
    phone = register_phone_entry.get()  # 입력된 전화번호를 가져옴

    # 파일에서 중복된 아이디 확인
    try:
        with open("C:/Users/User/Algorithm245/창업프로젝트1/users.txt", "r") as file:  # users.txt 파일을 읽기 모드로 열기
            for line in file:  # 파일의 각 줄에 대해 반복
                try:
                    stored_username, _, _, _ = line.strip().split(',')  # 저장된 사용자 이름을 읽기
                except ValueError:  # 줄의 형식이 올바르지 않으면 건너뜀
                    continue
                if username == stored_username:  # 입력된 사용자 이름이 저장된 사용자 이름과 일치하는지 확인
                    messagebox.showerror("회원가입 실패", "이미 존재하는 아이디입니다.")  # 중복된 사용자 이름일 경우 에러 메시지 표시
                    return  # 함수 종료
    except FileNotFoundError:
        # 파일이 없으면 무시하고 새로 생성
        pass

    # 파일에 회원 정보 저장
    with open("C:/Users/User/Algorithm245/창업프로젝트1/users.txt", "a") as file:  # users.txt 파일을 추가 모드로 열기
        file.write(f"{username},{password},{name},{phone}\n")  # 새로운 회원 정보를 파일에 쓰기
    messagebox.showinfo("회원가입 성공", "회원가입에 성공했습니다.")  # 회원가입 성공 메시지 표시



# 메인 윈도우 생성
root = tk.Tk()
root.title("관리자와 사용자 선택")
#root.geometry("300x200")

# 사용자와 관리자를 선택할 수 있는 버튼 생성
main_select_frame = tk.Frame(root)
user_button = tk.Button(main_select_frame, text="사용자", command=show_user_options)
user_button.grid(row=0, column=0, padx=10)
admin_button = tk.Button(main_select_frame, text="관리자")
admin_button.grid(row=0, column=1, padx=10)
main_select_frame.pack(pady=20)

# 사용자 로그인 및 회원가입을 선택할 수 있는 버튼 생성
user_select_frame = tk.Frame(root)
login_button = tk.Button(user_select_frame, text="로그인", command=show_login)
login_button.grid(row=0, column=0, padx=10)
register_button = tk.Button(user_select_frame, text="회원가입", command=show_register)
register_button.grid(row=0, column=1, padx=10)

# 사용자 로그인 창
login_frame = tk.Frame(root)
tk.Label(login_frame, text="아이디:").grid(row=0, column=0)
user_login_entry = tk.Entry(login_frame)
user_login_entry.grid(row=0, column=1)
tk.Label(login_frame, text="비밀번호:").grid(row=1, column=0)
user_login_password_entry = tk.Entry(login_frame, show="*")
user_login_password_entry.grid(row=1, column=1)
tk.Button(login_frame, text="로그인", command=user_login).grid(row=2, columnspan=2, pady=10)

# 회원가입 창
register_frame = tk.Frame(root)
tk.Label(register_frame, text="이름:").grid(row=0, column=0)
register_name_entry = tk.Entry(register_frame)
register_name_entry.grid(row=0, column=1)
tk.Label(register_frame, text="아이디:").grid(row=1, column=0)
register_username_entry = tk.Entry(register_frame)
register_username_entry.grid(row=1, column=1)
tk.Label(register_frame, text="비밀번호:").grid(row=2, column=0)
register_password_entry = tk.Entry(register_frame, show="*")
register_password_entry.grid(row=2, column=1)
tk.Label(register_frame, text="전화번호:").grid(row=3, column=0)
register_phone_entry = tk.Entry(register_frame)
register_phone_entry.grid(row=3, column=1)
tk.Button(register_frame, text="회원가입", command=register).grid(row=4, columnspan=2, pady=10)

# 메인 루프 실행
root.mainloop()