<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Connection"%>

<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.SQLException"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
	
<%@page import="java.util.List"%>
<%@page import="java.util.ArrayList"%>


<!DOCTYPE html>

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Stulist_autoFaceCheck</title>

</head>

<body>

	<%
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;

		String jdbcDriver = "jdbc:mysql://localhost:3306/autofacecheck?serverTimezone=UTC";
		String dbUser = "root";
		String dbPassword = "asd1234";
		
		List<String> tables = new ArrayList<String>();

		try {

			conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

			pstmt = conn.prepareStatement("show tables");

			rs = pstmt.executeQuery();

			while (rs.next()) {
				
				tables.add(rs.getString("Tables_in_autofacecheck"));
				
			}
			
		} catch (SQLException se) {
			
			se.printStackTrace();
			
		} finally {
			
			if (rs != null)
				rs.close();
			if (pstmt != null)
				pstmt.close();
			if (conn != null)
				conn.close();
			
		}
		
		for(int i=0;i<tables.size();i++){

			String str = tables.get(i).toString();
			if(str.equals("proflist")){
				continue;
			}
			else if(str.equals("profsubject")){
				continue;
			}
			else{
			
		%>
		
		<h2></h2>
	
	<table class=tables.get(i) border="1">
		<thead>
			<tr>
				<th colspan="3"><%= tables.get(i) %></th>
			</tr>
			<tr>
				<th width="200">출석시간</th>
				<th width="100">학번</th>
				<th width="100">이름</th>
			</tr>
		</thead>

		<tbody>

			<%
				try {

					conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

					pstmt = conn.prepareStatement("select * from "+ tables.get(i));

					rs = pstmt.executeQuery();

					while (rs.next()) {
			%>

			<tr>
				<td><%=rs.getTimestamp("attendTime")%></td>
				<td><%=rs.getInt("stuId")%></td>
				<td><%=rs.getString("stuName")%></td>
			</tr>

			<%
				}
				} catch (SQLException se) {
					se.printStackTrace();
				} finally {
					if (rs != null)
						rs.close();
					if (pstmt != null)
						pstmt.close();
					if (conn != null)
						conn.close();
				}
			%>

		</tbody>
	</table>
	
	<%}
			} %>
	
	
</body>

</html>