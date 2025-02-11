
# 取得 FHIR 資料庫的值

## 不需使用公用伺服器

1. 參照 `fhir_db` 資料夾內的 `docker-compose.yml`，將 `8080` 此 port 當作 FHIR 資料庫。
2. 輸入 `http://localhost:8080/fhir`。

## 使用 Appointment 資料表

1. Appointment 的 participant，若是需要 Patient 或是 Practitioner 作為 reference，FHIR 資料庫中務必先有以上資料，否則會報錯 400。

#### 備註

FHIR 資料庫中，每筆資料都會有自己的 `id`，此 `id` 代表進入 FHIR 資料庫的順序。
