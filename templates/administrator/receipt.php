<?php 
include 'db_connect.php';
include 'jdf.php';
$fees = $conn->query("SELECT ef.*,s.name as sname,s.id_no,concat(c.course,' - ',c.level) as `class` FROM student_ef_list ef inner join student s on s.id = ef.student_id inner join courses c on c.id = ef.course_id  where ef.id = {$_GET['ef_id']}");
foreach($fees->fetch_array() as $k => $v){
	$$k= $v;
}
$payments = $conn->query("SELECT * FROM payments where ef_id = $id ");
$pay_arr = array();
while($row=$payments->fetch_array()){
	$pay_arr[$row['id']] = $row;
}
?>

<style>
	.flex{
		display: inline-flex;
		width: 100%;
	}
	.w-50{
		width: 50%;
	}
	.text-center{
		text-align:center;
	}
	.text-right{
		text-align:right;
	}
	table.wborder{
		width: 100%;
		border-collapse: collapse;
	}
	table.wborder>tbody>tr, table.wborder>tbody>tr>td{
		border:1px solid;
	}
	p{
		margin:unset;
	}

</style>
<img style="width:10%; heigth:10%;" src="https://s8.uupload.ir/files/studying-student_90ie_c7nr.png" alt="سیستم هوشمند مدیریت سالن‌مطالعه">
<div class="container-fluid" style="direction: rtl; text-align: right; font-family: B Nazanin">
    <h2 style="direction: rtl; text-align: center; font-family: B Koodak">دبیرستان پسرانه مفتاح</h2>
    <h3 style="direction: rtl; text-align: center; font-family: B Koodak">سامانه هوشمند مدیریت سالن مطالعه</h3>
	<p class="text-center">سامانه مدیریت مالی</p>
	<hr>
	<div class="flex">
		<div class="w-50">
			<p>شماره فاکتور: <b><?php echo $ef_no ?></b></p>
			<p>دانش آموز: <b><?php echo ucwords($sname) ?></b></p>
			<p>سالن: <b><?php echo $class ?></b></p>
		</div>
		<?php if($_GET['pid'] > 0): ?>
		<div class="w-50">
			<p>ناریخ چاپ گزارش: <b><?php echo jdate("Y/m/d H:i:s");?></b></p>
			<p>مبلغ پرداختی(ریال): <b><?php echo isset($pay_arr[$_GET['pid']]) ? number_format($pay_arr[$_GET['pid']]['amount'],2): '' ?></b></p>
			<p>توضیحات: <b><?php echo isset($pay_arr[$_GET['pid']]) ? $pay_arr[$_GET['pid']]['remarks']: '' ?></b></p>
		</div>
		<?php endif; ?>
	</div>
	<hr>
	<p><b>گزارش پرداخت</b></p>
	<table class="wborder">
		<tr>
			<td width="50%">
				<p><b>اطلاعات شهریه</b></p>
				<hr>
				<table width="100%">
					<tr>
						<td width="50%">نوغ شهریه</td>
						<td width="50%" class='text-right'>مبلغ(ریال)</td>
					</tr>
					<?php 
				$cfees = $conn->query("SELECT * FROM fees where course_id = $course_id");
				$ftotal = 0;
				while ($row = $cfees->fetch_assoc()) {
					$ftotal += $row['amount'];
				?>
				<tr>
					<td><b><?php echo $row['description'] ?></b></td>
					<td class='text-right'><b><?php echo number_format($row['amount']) ?></b></td>
				</tr>
				<?php
				}
				?>
				<tr>
					<th>سر جمع</th>
					<th class='text-right'><b><?php echo number_format($ftotal) ?></b></th>
				</tr>
				</table>
			</td>			
			<td width="50%">
			<p><b>گزارش پرداخت ها</b></p>
				<table width="100%" class="wborder">
					<tr>
						<td width="50%">تاریخ</td>
						<td width="50%" class='text-right'>مبلغ(ریال)</td>
					</tr>
					<?php 
						$ptotal = 0;
						foreach ($pay_arr as $row) {
							if($row["id"] <= $_GET['pid'] || $_GET['pid'] == 0){
							$ptotal += $row['amount'];
					?>
					<tr>
						<td><b><?php echo $row['date_created'] ?></b></td>
						<td class='text-right'><b><?php echo number_format($row['amount']) ?></b></td>
					</tr>
					<?php
						}
						}
					?>
					<tr>
						<th>مبلغ کل(ریال)</th>
						<th class='text-right'><b><?php echo number_format($ptotal) ?></b></th>
					</tr>
				</table>
				<table width="100%">
					<tr>
						<td>مبلغ قابل پرداخت(ریال)</td>
						<td class='text-right'><b><?php echo number_format($ftotal) ?></b></td>
					</tr>
					<tr>
						<td>مبلغ پرداخت شده(ریال)</td>
						<td class='text-right'><b><?php echo number_format($ptotal) ?></b></td>
					</tr>
					<tr>
						<td>باقی مانده(ریال)</td>
						<td class='text-right'><b><?php echo number_format($ftotal-$ptotal) ?></b></td>
					</tr>
				</table>
			</td>			
		</tr>
	</table>
</div>