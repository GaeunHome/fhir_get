import requests

def read_fhir_appointments():
    url = "http://localhost:8080/fhir/Appointment"  # 替換成FHIR Appointment數據URL
    response = requests.get(url)
    fhir_data = response.json()

    # 獲得FHIR Appointment數據中的值
    for entry in fhir_data['entry']:
        appointment_description = entry['resource']['description']
        appointment_start = entry['resource']['start']
        appointment_end = entry['resource']['end']
        participant_actor_reference = entry['resource']['participant'][0]['actor']['reference']

        # 印出所有Appointment
        print("Appointment Description:", appointment_description)
        print("Appointment Start:", appointment_start)
        print("Appointment End:", appointment_end)
        print("Participant Actor Reference:", participant_actor_reference)
        print("-----------------------------------------------")

# 執行讀取FHIR Appointment數據的函式
read_fhir_appointments()
