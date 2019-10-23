<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Connection"%>

<%@page import="java.sql.Statement"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<%!  
	Connection conn = null;
	Statement stmt = null;
	
	//데이터 가져왔을 때,  저장시켜 놓을 객체를 만들자 : ResultSet
	ResultSet rs = null;
	
	//연결할 때, 정보 미리 만들기   jdbc:mysql://localhost:3306/autofacecheck
	String url = "jdbc:mysql://localhost:3306/autofacecheck";
	String user = "root";
	String pass = "asd1234";
	
	//stulist에서 데이터 가져오기
	String sql = "select * from stulist";
%>
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">
<title>Read Database Page</title>

</head>

<body>

<%@ page import = "java.sql.*, java.util.*" %>

MySQL 데이터 읽기

<%
try {
	Class.forName("com.mysql.jdbc.Driver");
	conn = DriverManager.getConnection(url, user, pass);
	out.println("DB연결성공!!");
	
	//conn을 통해서 sql을 실행할 수 있는 명령문 등록 객체를 생성
	stmt = conn.createStatement();
	//stmt 실제 명령을 수행  execute() => rs에 담아 놓으면 된다.
	rs = stmt.executeQuery(sql);
%>

<br><br>----------------------------------------<br>

<% while(rs.next()) { %>

<br> Time : <%= rs.getTimestamp("attendTime") %><br>
<br> StudentID : <%=rs.getInt("stuId") %><br>
<br> stuName : <%=rs.getString("stuName") %><br>

--------------------------------------------<br><br>

<%
} 
}catch (SQLException e) { %>

<% e.printStackTrace(); %>

<%	
} finally {
	try{
		if(rs != null) 	 rs.close();
		if(stmt != null) stmt.close();
		if(conn != null) conn.close();
	}catch(Exception e){
		e.printStackTrace();
	}
}
%>
</body>
</html>