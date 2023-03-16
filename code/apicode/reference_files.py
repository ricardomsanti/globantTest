hired_employees =   {      
                    "name" : "hired_employees", 
                    "cols": [
                                {"name": "id",
                                "datatype": "STRING",
                                "description": "Id of the employee"
                                },
                                {"name": "name",
                                "datatype": "INTEGER",
                                "description": "Name and surname of the employee"
                                },

                                {"name": "datetime",
                                "datatype": "STRING",
                                "description": "Hire datetime in ISO format"
                                },

                                {"name": "department_id",
                                "datatype": "INTEGER",
                                "description": "Id of the department which the employee was hired for"
                                },

                                {"name": "job_id",
                                "datatype": "INTEGER",
                                "description": "Id of the job which the employee was hired for"
                                }
                            ]
                    }

departments =   {      
                    "name" : "departments", 
                    "cols": [
                                {"name": "id",
                                "datatype": "INTEGER",
                                "description": "Id of the department"
                                },
                                {"name": "department",
                                "datatype": "STRING",
                                "description": "Name of the department"
                                }
                            ]
                }

jobs =  {      
            "name" : "departments", 
            "cols": [
                        {"name": "id",
                        "datatype": "INTEGER",
                        "description": "Id of the job"
                        },
                        {"name": "department",
                        "datatype": "STRING",
                        "description": "Name of the job"
                        }
                    ]
        }

