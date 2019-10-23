<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.PreparedStatement"%>

<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Stulist_autoFaceCheck</title>

</head>

<body>

MySQL 데이터 읽기

<table width="100%" border="1">

    <thead>
        <tr>
            <th>아이디</th>
            <th>이름</th>
        </tr>
    </thead>
    
    <tbody>
    
    <%
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
         
        try{
            String jdbcDriver = "jdbc:mysql://localhost:3306/autofacecheck?serverTimezone=UTC";
            String dbUser = "root";
            String dbPassword = "asd1234";
             
            conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);
             
            pstmt = conn.prepareStatement("select * from stulist");
             
            rs = pstmt.executeQuery();
             
            while(rs.next()){
    %>
    
        <tr>
            <td><%= rs.getInt("stuId") %></td>
            <td><%= rs.getString("stuName") %></td>
        </tr>
        
    <%
            }
        }catch(SQLException se){
            se.printStackTrace();
        }finally{
            if(rs != null) rs.close();
            if(pstmt != null) pstmt.close();
            if(conn != null) conn.close();
        }
    %>
    
    </tbody>
    
</table>

</body>

</html>