<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Connection"%>

<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.SQLException"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

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
	%>
	
	<h2></h2>
	
	<table class="stulist" width="200" border="1">
		<thead>
			<tr>
				<th colspan="2">출석부 명단</th>
			</tr>
			<tr>
				<th>아이디</th>
				<th>이름</th>
			</tr>
		</thead>

		<tbody>

			<%
				try {

					conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

					pstmt = conn.prepareStatement("select * from stulist");

					rs = pstmt.executeQuery();

					while (rs.next()) {
			%>

			<tr>
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
	
	<h2></h2>

	<table class="checknormality" width="200" border="1">
		<thead>
			<tr>
				<th colspan="2">출석자 명단</th>
			</tr>
			<tr>
				<th>아이디</th>
				<th>이름</th>
			</tr>
		</thead>

		<tbody>

			<%
				try {

					conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

					pstmt = conn.prepareStatement("select * from checknormality");

					rs = pstmt.executeQuery();

					while (rs.next()) {
			%>

			<tr>
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
	
	<h2></h2>

	<table class="checklate" width="200" border="1">
		<thead>
			<tr>
				<th colspan="2">지각자 명단</th>
			</tr>
			<tr>
				<th>아이디</th>
				<th>이름</th>
			</tr>
		</thead>

		<tbody>

			<%
				try {

					conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

					pstmt = conn.prepareStatement("select * from checklate");

					rs = pstmt.executeQuery();

					while (rs.next()) {
			%>

			<tr>
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
	
	<h2></h2>

	<table class="checkabsence" width="200" border="1">
		<thead>
			<tr>
				<th colspan="2">결석자 명단</th>
			</tr>
			<tr>
				<th>아이디</th>
				<th>이름</th>
			</tr>
		</thead>

		<tbody>

			<%
				try {

					conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPassword);

					pstmt = conn.prepareStatement("select * from checkabsence");

					rs = pstmt.executeQuery();

					while (rs.next()) {
			%>

			<tr>
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


</body>

</html>