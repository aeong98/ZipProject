## 사용안내
- 처음 python3 manage.py runserver 시에 나오는 화면은 상품추가 url만 표시함
- 회원가입폼과 상품추가 폼의 양식이 달라 한 화면에 띄우지 못함
- 아래 url을 주소창에 입력하여 접속시 문제 없음
- 해당 사항 참고 부탁드립니다!
<br>

## URL 정리
- 회원가입 : http://127.0.0.1:8000/users/auth/register
- 로그인 : http://127.0.0.1:8000/users/auth/login
- 로그아웃 : http://127.0.0.1:8000/users/auth/logout
- 소셜로그인-구글 : http://127.0.0.1:8000/users/auth/google
- 소셜로그인-네이버 : http://127.0.0.1:8000/users/auth/naver
<br>

- 상품추가 : http://127.0.0.1:8000/product/add
- 상품정보수정/삭제 : http://127.0.0.1:8000/product/add/n (n은 상품게시글의 id 값(숫자) / 예:http://127.0.0.1:8000/product/add/1)
- 상품댓글작성 : http://127.0.0.1:8000/product/comment
- 상품댓글수정/삭제 : http://127.0.0.1:8000/product/comment/n (n은 상품댓글의 id 값)
- 상품태그작성 : http://127.0.0.1:8000/product/tag (이 페이지에서 작성한 tag를 상품추가 페이지에서 선택 가능)
- 상품태그수정/삭제 : http://127.0.0.1:8000/product/tag/n (n은 상품태그의 id 값)
