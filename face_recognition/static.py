# 전역 변수

class staticVar():

    # 로그인 성공 시 교수님의 아이디와 이름을 저장해놓음
    # 과목 선택 창에서 해당 교수님 과목리스트를 가져오는데 사용됨
    profID = 0
    profName = '제이슨'
    
    # 반복되는 테이블명을 고정해서 사용하기 위함
    tableName = 'table_name'
    
    # 동적 출석 테이블 생성 시 사용될 단어들
    checkTable = 'checknormality'
    lateTable = 'checklate'
    absenceTable = 'checkabsence'

    # 출석 체크 정확도를 높이기 위한 딕셔너리 콜렉션
    checkDictionary = {}

    # 전체 인식된 횟수
    checkNumber = 0