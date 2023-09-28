# 取得FHIR資料庫的值
<h3>不需使用公用伺服器</h3>
<p>1. 參照fhir_db資料夾內的docker-compose.yml，將8080此port當作FHIR資料庫。</p>
<p>2. 輸入http://localhost:8080/fhir。</p>
<h3>使用Appointment資料表</h3>
<p>1. Appointment的participant，若是需要Patient或是Practitioner作為reference，FHIR資料庫中務必先有以上資料，否則會報錯400</p>
