{
"variables": [],
	"info": {
		"name": "HospitalManagementSystem",
		"_postman_id": "b0913fd0-ce54-8438-3f07-43ac142f2a1b",
		"description": "",
		"schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
	},
	"item": [
		{
			"name": "getPatient",
			"request": {
				"url": "http://127.0.0.1:5000/patient",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "addPatient",
			"request": {
				"url": "http://127.0.0.1:5000/patient",
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"pat_first_name\": \"Nancy\",\n  \"pat_last_name\": \"Joes\",\n  \"pat_insurance_no\": \"IN-3123\",\n  \"pat_ph_no\": \"2178013290\",\n  \"pat_address\": \"3 cadlelight 2\"\n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "updatePatient",
			"request": {
				"url": "http://127.0.0.1:5000/patient/2",
				"method": "PUT",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"pat_first_name\": \"Tushar\",\n  \"pat_last_name\": \"posst\",\n  \"pat_insurance_no\": \"posst\",\n  \"pat_ph_no\": \"posst\",\n  \"pat_address\": \"posst\"\n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "deletePatient",
			"request": {
				"url": "http://127.0.0.1:5000/patient/1",
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getDoctor",
			"request": {
				"url": "http://127.0.0.1:5000/doctor",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "addDoctor",
			"request": {
				"url": "http://127.0.0.1:5000/doctor",
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"doc_first_name\": \"Tony\",\n  \"doc_last_name\": \"Jonson\",\n  \"doc_ph_no\": \"9967544572\",\n  \"doc_address\": \"2 candlewood tree\"\n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "updateDoctor",
			"request": {
				"url": "http://127.0.0.1:5000/doctor/1",
				"method": "PUT",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"doc_first_name\": \"satish\",\n  \"doc_last_name\": \"posst\",\n  \"doc_ph_no\": \"posst\",\n  \"doc_address\": \"posst\"\n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "deleteDoctor",
			"request": {
				"url": "http://127.0.0.1:5000/doctor/1",
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getPatientById",
			"request": {
				"url": "http://127.0.0.1:5000/patient/2",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getDoctorById",
			"request": {
				"url": "http://127.0.0.1:5000/doctor/2",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "addAppointment",
			"request": {
				"url": "http://127.0.0.1:5000/appointment",
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"doc_id\": 1,\n  \"pat_id\": 1,\n  \"appointment_date\":\"2007-01-01 10:00:00\"\n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getAppointment",
			"request": {
				"url": "http://127.0.0.1:5000/appointment",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "updateAppoinetment",
			"request": {
				"url": "http://127.0.0.1:5000/appointment/1",
				"method": "PUT",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"description": ""
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"doc_id\":1,\n    \"pat_id\": 2\n    \n}"
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getAppointmentById",
			"request": {
				"url": "http://127.0.0.1:5000/appointment/1",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "deleteAppointment",
			"request": {
				"url": "http://127.0.0.1:5000/appointment/1",
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		},
		{
			"name": "getCount",
			"request": {
				"url": "http://127.0.0.1:5000/common",
				"method": "GET",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": []
				},
				"description": ""
			},
			"response": []
		}
	]
}
