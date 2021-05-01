import json

# Opening JSON file
json_text = '''
{
	"swagger": "2.0",
	"info": {
		"description": "交易银行智能知识引擎API",
		"version": "1.0",
		"title": "交易银行智能知识引擎API",
		"contact": {
			"name": "吴雪亮",
			"email": "xueliang.wu@cmb.com"
		}
	},
	"host": "localhost:8090",
	"basePath": "/",
	"tags": [{
		"name": "/annotationV2",
		"description": "Annotation Controller V 2"
	}, {
		"name": "/auth",
		"description": "Authorization API"
	}, {
		"name": "/dashboard/statistics_of_content",
		"description": "系统内容监控"
	}, {
		"name": "/data",
		"description": "Data Export Controller"
	}, {
		"name": "/file",
		"description": "file actions"
	}, {
		"name": "/fileV2",
		"description": "File Controller V 2"
	}, {
		"name": "/forum",
		"description": "Forum API"
	}, {
		"name": "/forumV2",
		"description": "Forum API"
	}, {
		"name": "/forumV2/config",
		"description": "Forum API"
	}, {
		"name": "/health/db",
		"description": "documents action"
	}, {
		"name": "/invite",
		"description": "Invite Controller"
	}, {
		"name": "/knowledge2",
		"description": "NK Controller"
	}, {
		"name": "/management/build",
		"description": "refresh builds"
	}, {
		"name": "/management/document",
		"description": "documents action"
	}, {
		"name": "/management/forum_board",
		"description": "forum board"
	}, {
		"name": "/management/forum_board_document",
		"description": "ForumBoard Document API"
	}, {
		"name": "/management/forum_event",
		"description": "forum and product mapping"
	}, {
		"name": "/management/forum_mapping",
		"description": "forum and product mapping"
	}, {
		"name": "/management/knowledge",
		"description": "Knowledge api"
	}, {
		"name": "/management/knowledge_category",
		"description": "Knowledge Category API"
	}, {
		"name": "/management/question_feedback",
		"description": "question_feedback api"
	}, {
		"name": "/management/system_feedback",
		"description": "sysetm feedback api"
	}, {
		"name": "/management/user_docgroup",
		"description": "UserController"
	}, {
		"name": "/messageV2",
		"description": "消息接口"
	}, {
		"name": "/model",
		"description": "Model Controller"
	}, {
		"name": "/notify",
		"description": "Notify Controller"
	}, {
		"name": "/openapi/document",
		"description": "Prm Document Controller"
	}, {
		"name": "/openapi/topic",
		"description": "Prm Stick Topic Controller"
	}, {
		"name": "/pc/floats",
		"description": "Forum Float Controller"
	}, {
		"name": "/pc/home",
		"description": "Pc Home Controller"
	}, {
		"name": "/pc/home/banner",
		"description": "Banner Controller"
	}, {
		"name": "/pc/news",
		"description": "News Controller"
	}, {
		"name": "/productV2",
		"description": "产品信息接口"
	}, {
		"name": "/search",
		"description": "Search and QA"
	}, {
		"name": "/searchV2",
		"description": "Search and QA for new UI version"
	}, {
		"name": "/userV2",
		"description": "'我的'頁面接口"
	}, {
		"name": "/ws",
		"description": "Web socket"
	}, {
		"name": "index-controller",
		"description": "Index Controller"
	}, {
		"name": "media-controller",
		"description": "media upload and download"
	}, {
		"name": "media-element-controller",
		"description": "Media element operation"
	}, {
		"name": "pc-index-controller",
		"description": "Pc Index Controller"
	}],
	"paths": {
		"/": {
			"get": {
				"tags": ["index-controller"],
				"summary": "ystLogin",
				"operationId": "ystLoginUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}, {
					"name": "data",
					"in": "query",
					"description": "data",
					"required": false,
					"type": "string"
				}, {
					"name": "token",
					"in": "query",
					"description": "token",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/allUploadQAs": {
			"get": {
				"tags": ["/annotationV2"],
				"summary": "allUploadQAs",
				"operationId": "allUploadQAsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "comment",
					"in": "query",
					"description": "comment",
					"required": false,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "question",
					"in": "query",
					"description": "question",
					"required": false,
					"type": "string"
				}, {
					"name": "userName",
					"in": "query",
					"description": "userName",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«AnnotationContextInfo»»",
							"originalRef": "CommonResult«PaginationInfo«AnnotationContextInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/deleteAnnotationQuestion": {
			"post": {
				"tags": ["/annotationV2"],
				"summary": "deleteAnnotationQuestion",
				"operationId": "deleteAnnotationQuestionUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "annotationId",
					"in": "query",
					"description": "annotationId",
					"required": true,
					"type": "string"
				}, {
					"name": "questionId",
					"in": "query",
					"description": "questionId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«boolean»",
							"originalRef": "CommonResult«boolean»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/downloadQAExcelFile": {
			"post": {
				"tags": ["/annotationV2"],
				"summary": "downloadQAExcelFile",
				"operationId": "downloadQAExcelFileUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fileName",
					"in": "query",
					"description": "fileName",
					"required": true,
					"type": "string"
				}, {
					"name": "fileSerialsNo",
					"in": "query",
					"description": "fileSerialsNo",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ResponseEntity",
							"originalRef": "ResponseEntity"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/downloadQATemplate": {
			"post": {
				"tags": ["/annotationV2"],
				"summary": "downloadQATemplate",
				"operationId": "downloadQATemplateUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ResponseEntity",
							"originalRef": "ResponseEntity"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/queryUploadQARecords": {
			"get": {
				"tags": ["/annotationV2"],
				"summary": "queryUploadQARecords",
				"operationId": "queryUploadQARecordsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "comment",
					"in": "query",
					"description": "comment",
					"required": false,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userName",
					"in": "query",
					"description": "userName",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«QAUploadRecord»»",
							"originalRef": "CommonResult«PaginationInfo«QAUploadRecord»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/annotationV2/uploadQA": {
			"post": {
				"tags": ["/annotationV2"],
				"summary": "uploadQA",
				"operationId": "uploadQAUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "comment",
					"in": "query",
					"description": "comment",
					"required": false,
					"type": "string"
				}, {
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/app/**": {
			"get": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingHEAD",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingPUT",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingDELETE",
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingOPTIONS",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["index-controller"],
				"summary": "index",
				"operationId": "indexUsingPATCH",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "map",
					"in": "query",
					"description": "map",
					"required": false,
					"type": "object"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/addUser": {
			"post": {
				"tags": ["/auth"],
				"summary": "add user",
				"operationId": "addUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "departname",
					"in": "query",
					"description": "departname",
					"required": true,
					"type": "string"
				}, {
					"name": "identity",
					"in": "query",
					"description": "identity",
					"required": true,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "string"
				}, {
					"name": "username",
					"in": "query",
					"description": "username",
					"required": true,
					"type": "string"
				}, {
					"name": "ystId",
					"in": "query",
					"description": "ystId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/clean": {
			"post": {
				"tags": ["/auth"],
				"summary": "Clean All User Data",
				"operationId": "cleanMemoryUserDataUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/currentUserId": {
			"get": {
				"tags": ["/auth"],
				"summary": "Get Current login userId",
				"operationId": "currentUserUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/generatePcUrl": {
			"post": {
				"tags": ["/auth"],
				"summary": "(For Test Pc) generate yst mock url",
				"operationId": "generatePcUrlUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "sapid",
					"in": "query",
					"description": "sapid",
					"required": true,
					"type": "array",
					"items": {
						"type": "string"
					},
					"collectionFormat": "multi"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/generateToken": {
			"get": {
				"tags": ["/auth"],
				"summary": "(For Test) generate token",
				"operationId": "generateTokenUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": true,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/generateYstUrl": {
			"get": {
				"tags": ["/auth"],
				"summary": "(For Test) generate yst mock url",
				"operationId": "generateYstUrlUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/listAllUser": {
			"post": {
				"tags": ["/auth"],
				"summary": "get all user",
				"operationId": "findAllUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/listAllUserGroup": {
			"post": {
				"tags": ["/auth"],
				"summary": "get all group",
				"operationId": "findAllUserGroupUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/listAllUserRole": {
			"post": {
				"tags": ["/auth"],
				"summary": "get all rule",
				"operationId": "findAllUserRoleUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/syncYstData": {
			"post": {
				"tags": ["/auth"],
				"summary": "Sync Yst data",
				"operationId": "syncYstUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/syncYstUserHeaderImage": {
			"post": {
				"tags": ["/auth"],
				"summary": "Sync Yst data",
				"operationId": "syncYstUserHeaderImageUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/updatePermission": {
			"post": {
				"tags": ["/auth"],
				"summary": "update permission",
				"operationId": "updatePermissionUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "permission",
					"in": "query",
					"description": "permission",
					"required": true,
					"items": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/auth/updateUserRole": {
			"post": {
				"tags": ["/auth"],
				"summary": "update userRole",
				"operationId": "updateUserRoleUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "roleId",
					"in": "query",
					"description": "roleId",
					"required": true,
					"type": "array",
					"items": {
						"type": "string"
					},
					"collectionFormat": "multi"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/bbs": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "redirectBbs",
				"operationId": "redirectBbsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/dashboard/content_statistical/query": {
			"get": {
				"tags": ["/dashboard/statistics_of_content"],
				"summary": "统计数据查询",
				"operationId": "queryUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "endDate",
					"in": "query",
					"description": "结束日期",
					"required": false,
					"type": "string",
					"x-example": "2020-06-03"
				}, {
					"name": "startDate",
					"in": "query",
					"description": "起始日期",
					"required": false,
					"type": "string",
					"x-example": "2018-05-03"
				}, {
					"name": "statisticsType",
					"in": "query",
					"description": "统计类别",
					"required": true,
					"type": "string",
					"x-example": "SUMMARY_BY_DOC_FILE",
					"enum": ["SUMMARY_BY_DOC_FILE", "SUMMARY_BY_KNOWLEDGE", "SUMMARY_BY_QA", "SUMMARY_BY_THREAD", "SUMMARY_BY_THREAD_OF_NO_REPLY", "SUMMARY_BY_THREAD_OF_HAS_REPLY", "SUMMARY_FORUM_TOP10", "SUMMARY_THREAD_BY_BOARD", "SUMMARY_DOC_FILE_BY_OUT_OF_DATE", "SUMMARY_SYSTEM_PV", "SUMMARY_SYSTEM_UV", "SUMMARY_SYSTEM_DEVICE", "SUMMARY_SYSTEM_TOP", "SUMMARY_KNOWLEDGE_PV", "SUMMARY_KNOWLEDGE_UV", "SUMMARY_SEARCH_BY_DEVICE", "SUMMARY_SEARCH_PV", "SUMMARY_SEARCH_UV"]
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«StatisticsChart»",
							"originalRef": "CommonResult«StatisticsChart»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/data/export/doc": {
			"get": {
				"tags": ["/data"],
				"summary": "根据给定的时间导出所有的文件信息",
				"description": "接口负责人：陈玉环",
				"operationId": "downloadDocUsingGET",
				"consumes": ["*/*"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "endTime",
					"in": "query",
					"description": "endTime",
					"required": true,
					"type": "string"
				}, {
					"name": "startTime",
					"in": "query",
					"description": "startTime",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/data/export/docKnowledge": {
			"get": {
				"tags": ["/data"],
				"summary": "根据给定的文件id导出文件的所有知识信息",
				"description": "接口负责人：陈玉环",
				"operationId": "downloadDocumentKnowledgeUsingGET",
				"consumes": ["*/*"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fileId",
					"in": "query",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/doc": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "redirectDocument",
				"operationId": "redirectDocumentUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/docContent/{fileId}/pdf_data": {
			"get": {
				"tags": ["/file"],
				"summary": "/docContent",
				"operationId": "queryFileContentUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "fileId",
					"in": "path",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/download/{fileId}": {
			"get": {
				"tags": ["/file"],
				"summary": "document file",
				"operationId": "downloadFileUsingGET",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "fileId",
					"in": "path",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/downloadDocument/{fileId}": {
			"get": {
				"tags": ["/file"],
				"summary": "document stream",
				"operationId": "downloadFileContentUsingGET_1",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "fileId",
					"in": "path",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/fileLocation": {
			"get": {
				"tags": ["/file"],
				"summary": "/fileLocation",
				"operationId": "fileLocationUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/getHtmlContentOfFile/{fileId}": {
			"get": {
				"tags": ["/file"],
				"summary": "getHtmlContentOfPpt",
				"operationId": "getHtmlContentOfPptUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "fileId",
					"in": "path",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/file/getHtmlContentOfWord/{fileId}": {
			"get": {
				"tags": ["/file"],
				"summary": "getHtmlContentOfWord",
				"operationId": "getHtmlContentOfWordUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "fileId",
					"in": "path",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/fileV2/deleteAttachMentById": {
			"get": {
				"tags": ["/fileV2"],
				"summary": "删除附件",
				"operationId": "deleteAttachMentUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "attachMentId",
					"in": "query",
					"description": "附件id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/fileV2/downloadFile": {
			"get": {
				"tags": ["/fileV2"],
				"summary": "从ecs中下载一个文件",
				"description": "接口负责人：刘乐乐",
				"operationId": "downloadFileUsingGET_1",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "downloadName",
					"in": "query",
					"description": "文件下载名",
					"required": true,
					"type": "string"
				}, {
					"name": "fileName",
					"in": "query",
					"description": "文件名",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/fileV2/previewFile/{pdfName}": {
			"get": {
				"tags": ["/fileV2"],
				"summary": "PDF加水印后返回",
				"description": "接口负责人：刘乐乐",
				"operationId": "previewFileUsingGET",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "fileName",
					"in": "query",
					"description": "fileName",
					"required": false,
					"type": "string"
				}, {
					"name": "pdfName",
					"in": "path",
					"description": "pdfName",
					"required": true,
					"type": "string"
				}, {
					"name": "requiredMark",
					"in": "query",
					"description": "requiredMark",
					"required": false,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/fileV2/uploadFile": {
			"post": {
				"tags": ["/fileV2"],
				"summary": "上传一个新文件到ecs中",
				"description": "接口负责人：刘乐乐",
				"operationId": "uploadFileUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/adapterBase64OfPost": {
			"post": {
				"tags": ["/forum"],
				"summary": "把所有post的图片转化为url形式",
				"operationId": "adapterBase64OfPostUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/deletePost": {
			"post": {
				"tags": ["/forum"],
				"summary": "删除帖子",
				"operationId": "deletePostUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/NewPostRequest",
						"originalRef": "NewPostRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostInfo»",
							"originalRef": "CommonResult«ForumPostInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/editPost": {
			"post": {
				"tags": ["/forum"],
				"summary": "编辑主题帖",
				"operationId": "editPostUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/NewPostRequest",
						"originalRef": "NewPostRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostInfo»",
							"originalRef": "CommonResult«ForumPostInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/followBoard": {
			"get": {
				"tags": ["/forum"],
				"summary": "关注板块",
				"operationId": "followBoardUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumBoardInfo»»",
							"originalRef": "CommonResult«List«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/getBbsBaseURL": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取BBS URL",
				"operationId": "getBbsBaseURLUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/getForumBoardDetail": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取板块的详细信息",
				"operationId": "getForumBoardDetailUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "boardId",
					"in": "query",
					"description": "boardId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumBoardDetailInfo»",
							"originalRef": "CommonResult«ForumBoardDetailInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/getGlobalSiteInfo": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取全站信息，看一下是否前端在使用，没用的话可以删除",
				"operationId": "getGlobalSiteInfoUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«GlobalSiteInfo»",
							"originalRef": "CommonResult«GlobalSiteInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/getUserFollowedBoards": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取用户关注的板块",
				"operationId": "getUserFollowedBoardsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«FollowedForumBoardInfo»»",
							"originalRef": "CommonResult«List«FollowedForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/newPost": {
			"post": {
				"tags": ["/forum"],
				"summary": "newPost",
				"operationId": "newPostUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/NewPostRequest",
						"originalRef": "NewPostRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostInfo»",
							"originalRef": "CommonResult«ForumPostInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/postFavorite": {
			"post": {
				"tags": ["/forum"],
				"summary": "postFavorite",
				"operationId": "postFavoriteUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "postFavoriteRequest",
					"description": "postFavoriteRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/PostFavoriteRequest",
						"originalRef": "PostFavoriteRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/postLike": {
			"post": {
				"tags": ["/forum"],
				"summary": "postLike",
				"operationId": "postLikeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "postLikeRequest",
					"description": "postLikeRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/PostLikeRequest",
						"originalRef": "PostLikeRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/postPoll": {
			"post": {
				"tags": ["/forum"],
				"summary": "postPoll",
				"operationId": "postPollUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "pollRequest",
					"description": "pollRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/PollRequest",
						"originalRef": "PollRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPollVo»",
							"originalRef": "CommonResult«ForumPollVo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryBoardEssentialThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryBoardEssentialThreads",
				"operationId": "queryBoardEssentialThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryBoardEvents": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryBoardEvents",
				"operationId": "queryBoardEventsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumEventInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumEventInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryBoardHotThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取板块的热门帖",
				"operationId": "queryBoardHotThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryBoardNormalThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryBoardNormalThreads",
				"operationId": "queryBoardNormalThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryBoardTopThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryBoardTopThreads",
				"operationId": "queryBoardTopThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryNewsPosts": {
			"get": {
				"tags": ["/forum"],
				"summary": "根据主题id查询资讯帖子",
				"operationId": "queryNewsPostsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "messageId",
					"in": "query",
					"description": "此字段已过时,不用",
					"required": false,
					"type": "ref"
				}, {
					"name": "orderByTop",
					"in": "query",
					"description": "按置顶排序传1，按回答时间默认0",
					"required": false,
					"type": "ref",
					"default": "0"
				}, {
					"name": "tid",
					"in": "query",
					"description": "1829",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryPollInfo": {
			"get": {
				"tags": ["/forum"],
				"summary": "根据tid查询投票信息",
				"operationId": "queryPollInfoUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "tid",
					"in": "query",
					"description": "tid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPollVo»",
							"originalRef": "CommonResult«ForumPollVo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryPosts": {
			"get": {
				"tags": ["/forum"],
				"summary": "根据主题id查询帖子",
				"operationId": "queryPostsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "orderByTop",
					"in": "query",
					"description": "orderByTop",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "tid",
					"in": "query",
					"description": "tid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserCredit": {
			"get": {
				"tags": ["/forum"],
				"summary": "获取用户积分",
				"operationId": "queryUserCreditUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserFollowedBoards": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryUserFollowedBoards",
				"operationId": "queryUserFollowedBoardsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "topN",
					"in": "query",
					"description": "topN",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumBoardInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserHistoryThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryUserHistoryThreads",
				"operationId": "queryUserHistoryThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserMyMessage": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryUserMyMessage",
				"operationId": "queryUserMyMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "PageSize",
					"in": "query",
					"description": "PageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«NotificationInfo»»",
							"originalRef": "CommonResult«PaginationInfo«NotificationInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserReplyThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryUserReplyThreads",
				"operationId": "queryUserReplyThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryUserSentThreads": {
			"get": {
				"tags": ["/forum"],
				"summary": "queryUserSentThreads",
				"operationId": "queryUserSentThreadsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/queryVoter": {
			"get": {
				"tags": ["/forum"],
				"summary": "根据tid查询投票参与人",
				"operationId": "queryVoterUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "tid",
					"in": "query",
					"description": "tid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumVoterInfo»»",
							"originalRef": "CommonResult«List«ForumVoterInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forum/replayPost": {
			"post": {
				"tags": ["/forum"],
				"summary": "replayPost",
				"operationId": "replayPostUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "replayRequest",
					"description": "replayRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ReplayRequest",
						"originalRef": "ReplayRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostInfo»",
							"originalRef": "CommonResult«ForumPostInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/addForumTag": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "addForumTag",
				"operationId": "addForumTagUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "forumTagInfo",
					"description": "forumTagInfo",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumTagInfo»",
							"originalRef": "CommonResult«ForumTagInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/config/updateStatusById": {
			"get": {
				"tags": ["/forumV2/config"],
				"summary": "设置帖子的属性",
				"description": "接口负责人：xw80329",
				"operationId": "updateStatusByIdUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "action",
					"in": "query",
					"description": "POST_TOP",
					"required": true,
					"type": "string",
					"enum": ["POST_TOP", "CANCEL_POST_TOP", "TOP_MODIFIED_TIME", "CANCEL_TOP_MODIFIED_TIME", "POST_LIMITED_TOP", "CANCEL_POST_LIMITED_TOP", "POST_ESSENTIAL", "CANCEL_POST_ESSENTIAL", "POST_LIMITED_ESSENTIAL", "CANCEL_POST_LIMITED_ESSENTIAL", "DELETE_THREAD", "CANCEL_DELETE_THREAD", "DELETE_REPLY", "CANCEL_DELETE_REPLY", "THREAD_FLOAT", "CANCEL_THREAD_FLOAT", "DELETE_POST", "CANCEL_DELETE_POST"]
				}, {
					"name": "entityId",
					"in": "query",
					"description": "123",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "expirationDays",
					"in": "query",
					"description": "10",
					"required": false,
					"type": "ref"
				}, {
					"name": "reason",
					"in": "query",
					"description": "帖子内容有问题",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/countPostReplies": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "查询评论的回复的条数",
				"description": "接口负责人：陈玉环",
				"operationId": "countPostRepliesUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "postId",
					"in": "query",
					"description": "postId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/deleteForumTag": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "deleteForumTag",
				"operationId": "deleteForumTagUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "tagIds",
					"in": "query",
					"description": "tagIds",
					"required": true,
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					},
					"collectionFormat": "multi"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumTagInfo»",
							"originalRef": "CommonResult«ForumTagInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/editForumTag": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "editForumTag",
				"operationId": "editForumTagUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "forumTagInfo",
					"description": "forumTagInfo",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumTagInfo»",
							"originalRef": "CommonResult«ForumTagInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/editPostV2": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "编辑主题帖",
				"operationId": "editPostUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/NewPostRequest",
						"originalRef": "NewPostRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostInfo»",
							"originalRef": "CommonResult«ForumPostInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/followBoard": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "followBoard",
				"operationId": "followBoardUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "fids",
					"required": true,
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					},
					"collectionFormat": "multi"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumBoardInfo»»",
							"originalRef": "CommonResult«List«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/getGlobalBoards": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "queryBoards",
				"operationId": "queryBoardsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/getQAForPost": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "根据帖子的主题Id获取提问帖的QA对",
				"description": "接口负责人：陈玉环",
				"operationId": "getQAForPostUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "threadId",
					"in": "query",
					"description": "threadId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumQAFileConnectionInfo»",
							"originalRef": "CommonResult«ForumQAFileConnectionInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/getUserInfo": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "getUserInfo",
				"operationId": "getUserInfoUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "icon",
					"in": "query",
					"description": "icon",
					"required": false,
					"type": "boolean"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«UserSiteInfo»",
							"originalRef": "CommonResult«UserSiteInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/noReplyPost": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "帖子暂无回答接口",
				"operationId": "noReplyPostUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "120,113",
					"required": false,
					"type": "string"
				}, {
					"name": "isDispose",
					"in": "query",
					"description": "1/0",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "relatedMe",
					"in": "query",
					"description": "1/0",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/operateQA": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "对帖子上的QA对进行操作，包括新建和编辑",
				"description": "接口负责人：陈玉环",
				"operationId": "operateQAUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "forumQAFileConnection",
					"description": "forumQAFileConnection",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ForumQAFileConnectionInfo",
						"originalRef": "ForumQAFileConnectionInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumQAFileConnectionInfo»",
							"originalRef": "CommonResult«ForumQAFileConnectionInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryAllFavoriteForumTag": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "获取当前用户关注所有板块下的论坛标签",
				"description": "接口负责人：WangYong",
				"operationId": "queryAllFavoriteForumTagUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumTagInfo»»",
							"originalRef": "CommonResult«List«ForumTagInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryAllForumTag": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "queryAllForumTag",
				"operationId": "queryAllForumTagUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumTagInfo»»",
							"originalRef": "CommonResult«List«ForumTagInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryAllProductForumTag": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "根据产品获取论坛标签",
				"description": "接口负责人：WangYong",
				"operationId": "queryAllProductForumTagUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "120,113",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumTagInfo»»",
							"originalRef": "CommonResult«List«ForumTagInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryAllRelatedDiscussionPost": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "根据标签-相关讨论、相关问题",
				"description": "接口负责人：WangYong",
				"operationId": "queryAllRelatedDiscussionPostUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "5",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "special",
					"in": "query",
					"description": "0/8",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "tid",
					"in": "query",
					"description": "1634/1636",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumPostInfo»»",
							"originalRef": "CommonResult«List«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryDeletedPost": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "帖子已删除接口",
				"operationId": "queryDeletedPostUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "120,113",
					"required": false,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "relatedMe",
					"in": "query",
					"description": "1/0",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryEssentialThreads": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "查询精华贴",
				"description": "接口负责人：xw80329",
				"operationId": "queryBoardEssentialThreadsUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "eggShellable",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}, {
					"name": "fids",
					"in": "query",
					"description": "10,13",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "products",
					"in": "query",
					"description": "12,13",
					"required": false,
					"type": "string"
				}, {
					"name": "tags",
					"in": "query",
					"description": "1459,1899",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumThreadInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumThreadInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryFilterConditions": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "queryFilterConditions",
				"operationId": "queryFilterConditionsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "onlyUserFollowed",
					"in": "query",
					"description": "onlyUserFollowed",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryHotThreads": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "查询热门帖子，按更新时间排序",
				"description": "接口负责人：xw80329",
				"operationId": "queryBoardHotThreadsUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "eggShellable",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}, {
					"name": "fids",
					"in": "query",
					"description": "10,13",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "products",
					"in": "query",
					"description": "12,13",
					"required": false,
					"type": "string"
				}, {
					"name": "tags",
					"in": "query",
					"description": "1459,1899",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryMyManagementCount": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "我的管理统计",
				"operationId": "queryMyManagementCountUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "120,113",
					"required": false,
					"type": "string"
				}, {
					"name": "relatedMe",
					"in": "query",
					"description": "1/0",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryNormalThreads": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "查询帖子，按更新时间排序",
				"description": "接口负责人：xw80329",
				"operationId": "queryBoardNormalThreadsUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "eggShellable",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}, {
					"name": "fids",
					"in": "query",
					"description": "10,13",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "products",
					"in": "query",
					"description": "12,13",
					"required": false,
					"type": "string"
				}, {
					"name": "tags",
					"in": "query",
					"description": "1459,1899",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryQA": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "我的管理查询QA",
				"operationId": "queryQAUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "120,75",
					"required": false,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "relatedMe",
					"in": "query",
					"description": "1/0",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumQAFileConnectionDTO»»",
							"originalRef": "CommonResult«PaginationInfo«ForumQAFileConnectionDTO»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryRecentVotingPosts": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "获取近期投票贴",
				"description": "接口负责人：WangYong",
				"operationId": "queryRecentVotingPostsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "5",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumPostInfo»»",
							"originalRef": "CommonResult«List«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/queryReplayDeep": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "查询评论的回复",
				"description": "接口负责人：陈玉环",
				"operationId": "queryReplayDeepUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "postId",
					"in": "query",
					"description": "postId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostReplayInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostReplayInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/replayDeep": {
			"post": {
				"tags": ["/forumV2"],
				"summary": "对评论及回复进行回复",
				"description": "接口负责人：陈玉环",
				"operationId": "replayDeepUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "replayRequest",
					"description": "replayRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ReplayRequest",
						"originalRef": "ReplayRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumPostReplayInfo»",
							"originalRef": "CommonResult«ForumPostReplayInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/searchForumTag": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "searchForumTag",
				"operationId": "searchForumTagUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "querySize",
					"in": "query",
					"description": "querySize",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "queryString",
					"in": "query",
					"description": "queryString",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumTagInfo»»",
							"originalRef": "CommonResult«List«ForumTagInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/searchQuestionPosts": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "searchQuestionPosts",
				"operationId": "searchQuestionPostsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "querySize",
					"in": "query",
					"description": "querySize",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "queryString",
					"in": "query",
					"description": "queryString",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/forumV2/unfollowBoard": {
			"get": {
				"tags": ["/forumV2"],
				"summary": "unfollowBoard",
				"operationId": "unfollowBoardUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "fids",
					"required": true,
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					},
					"collectionFormat": "multi"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/getMedia": {
			"get": {
				"tags": ["media-controller"],
				"summary": "getMedia",
				"operationId": "getMediaUsingGET_1",
				"produces": ["image/png"],
				"parameters": [{
					"name": "mediaId",
					"in": "query",
					"description": "mediaId",
					"required": true,
					"type": "string"
				}, {
					"name": "original",
					"in": "query",
					"description": "original",
					"required": false,
					"type": "string"
				}, {
					"name": "sourceId",
					"in": "query",
					"description": "sourceId",
					"required": false,
					"type": "string"
				}, {
					"name": "sourceType",
					"in": "query",
					"description": "sourceType",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"type": "string",
							"format": "byte"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/getMediaOfEmptyUser": {
			"get": {
				"tags": ["media-controller"],
				"summary": "getMediaOfEmptyUser",
				"operationId": "getMediaUsingGET",
				"produces": ["image/png"],
				"parameters": [{
					"name": "mediaId",
					"in": "query",
					"description": "mediaId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"type": "string",
							"format": "byte"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/health/db/data": {
			"get": {
				"tags": ["/health/db"],
				"summary": "document stream",
				"operationId": "downloadFileContentUsingGET",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "sql",
					"in": "query",
					"description": "sql",
					"required": true,
					"type": "string"
				}, {
					"name": "zipFormat",
					"in": "query",
					"description": "zipFormat",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/health/db/upload": {
			"post": {
				"tags": ["/health/db"],
				"summary": "execute",
				"operationId": "executeScriptUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}, {
					"name": "signature",
					"in": "query",
					"description": "signature",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/invite/InviteReply": {
			"post": {
				"tags": ["/invite"],
				"summary": "管理员/版主 邀请其他用户来回来提问帖接口",
				"operationId": "inviteReplyUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "inviteRequest",
					"description": "inviteRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/InviteRequest",
						"originalRef": "InviteRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/invite/getInvitees": {
			"get": {
				"tags": ["/invite"],
				"summary": "获取可邀请的用户集合",
				"operationId": "getInviteesUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "75",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "nameStr",
					"in": "query",
					"description": "admin",
					"required": false,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "tid",
					"in": "query",
					"description": "1",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/invite/queryInviteReply": {
			"get": {
				"tags": ["/invite"],
				"summary": "获取邀请‘我’回答",
				"operationId": "queryInviteReplyUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userId",
					"in": "query",
					"description": "1",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/kc": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "redirectKnowledge",
				"operationId": "redirectKnowledgeUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/kcLogin": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "knowledgeLogin",
				"operationId": "knowledgeLoginUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge/changePassword": {
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "changePassword",
				"operationId": "changePasswordUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "newPassword",
					"in": "query",
					"description": "newPassword",
					"required": false,
					"type": "string"
				}, {
					"name": "oldPassword",
					"in": "query",
					"description": "oldPassword",
					"required": false,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge/login": {
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "knowledgeLogin",
				"operationId": "knowledgeLoginUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "password",
					"in": "query",
					"description": "password",
					"required": false,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/commitAnnotation": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "commitAnnotation",
				"operationId": "commitAnnotationUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "annotationId",
					"in": "query",
					"description": "annotationId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/commitKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "commitKnowledge",
				"operationId": "commitKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "knowledge",
					"description": "knowledge",
					"required": true,
					"schema": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/confirmAllKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "confirmAllKnowledge",
				"operationId": "confirmKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/confirmAnnotation": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "confirmAnnotation",
				"operationId": "confirmAnnotationUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "annotationContextInfo",
					"description": "标注",
					"required": true,
					"schema": {
						"$ref": "#/definitions/AnnotationContextInfo",
						"originalRef": "AnnotationContextInfo"
					}
				}, {
					"name": "status",
					"in": "query",
					"description": "拒绝0/通过1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/confirmKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "confirmKnowledge",
				"operationId": "confirmKnowledgeUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "knowledge",
					"description": "知识",
					"required": true,
					"schema": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				}, {
					"name": "status",
					"in": "query",
					"description": "拒绝0/通过1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/countAnnotation": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "countAnnotation",
				"operationId": "countAnnotationContextUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/countKnowledge": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "countKnowledge",
				"operationId": "countKnowledgeUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/deleteAnnotationContext": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "deleteAnnotationContext",
				"operationId": "deleteAnnotationContextUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "annotationContext",
					"description": "annotationContext",
					"required": true,
					"schema": {
						"$ref": "#/definitions/AnnotationContextInfo",
						"originalRef": "AnnotationContextInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«AnnotationContextInfo»",
							"originalRef": "CommonResult«AnnotationContextInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/deleteKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "deleteKnowledge",
				"operationId": "deleteKnowledgeUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "knowledge",
					"description": "knowledge",
					"required": true,
					"schema": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/deleteKnowledgeByDocId": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "deleteKnowledgeByDocId",
				"operationId": "deleteKnowledgeByDocIdUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "documentId",
					"in": "query",
					"description": "documentId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/download": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "download",
				"operationId": "downloadUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ResponseEntity",
							"originalRef": "ResponseEntity"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/filterKnowledgeByCondition": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "filterKnowledgeByCondition",
				"operationId": "filterKnowledgeByConditionUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "documentId",
					"in": "query",
					"description": "documentId",
					"required": true,
					"type": "string"
				}, {
					"name": "filterType",
					"in": "query",
					"description": "filterType",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/newEmptyAnnotationContext": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "newEmptyAnnotationContext",
				"operationId": "newEmptyAnnotationContextUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«AnnotationContext»",
							"originalRef": "CommonResult«AnnotationContext»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": true
			}
		},
		"/knowledge2/newEmptyKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "newEmptyKnowledge click plus + ",
				"operationId": "newEmptyKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "displayOrder",
					"in": "query",
					"description": "displayOrder",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "sourceId",
					"in": "query",
					"description": "sourceId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/nlpKeyword": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "nlpKeyword",
				"operationId": "nlpKeywordUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/nlpNewWords": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "nlpNewWords",
				"operationId": "nlpNewWordsUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/nlpSlot": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "nlpSlot",
				"operationId": "nlpSlotUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/nlpTask": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "nlpTask",
				"operationId": "nlpTaskUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/orderKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "orderKnowledge",
				"operationId": "orderKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "currentKnowledge",
					"description": "currentKnowledge",
					"required": true,
					"schema": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				}, {
					"name": "newOrder",
					"in": "query",
					"description": "newOrder",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryAllKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "query all knowledge with pagination",
				"operationId": "queryAllKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«KnowledgeInfo»»",
							"originalRef": "CommonResult«PaginationInfo«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryAllQuestions": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "query all questions",
				"operationId": "queryAllQuestionUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«AnnotationContextInfo»»",
							"originalRef": "CommonResult«PaginationInfo«AnnotationContextInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryAnnotationContext": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "query AnnotationContext by knowledge id with completed knowledge info",
				"operationId": "queryAnnotationContextUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryAnnotationContextByDocId": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "query all knowledge's annotations by document id",
				"operationId": "queryAnnotationContextByDocIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "documentId",
					"in": "query",
					"description": "documentId",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryKnowledge": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "query knowledge by document id",
				"operationId": "queryKnowledgeUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "documentId",
					"in": "query",
					"description": "documentId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/queryKnowledgeById": {
			"get": {
				"tags": ["/knowledge2"],
				"summary": "query knowledge by knowledge id",
				"operationId": "queryKnowledgeByIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/splitDoc": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "splitDoc",
				"operationId": "splitDocUsingPOST_1",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}, {
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": false,
					"type": "file"
				}, {
					"name": "splitType",
					"in": "query",
					"description": "splitType",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/updateAnnotationContexts": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "updateAnnotationContexts",
				"operationId": "updateAnnotationContextsUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "annotationContexts",
					"description": "annotationContexts",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/AnnotationContextInfo",
							"originalRef": "AnnotationContextInfo"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«AnnotationContextInfo»",
							"originalRef": "CommonResult«AnnotationContextInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/knowledge2/updateKnowledge": {
			"post": {
				"tags": ["/knowledge2"],
				"summary": "updateKnowledge",
				"operationId": "updateKnowledgeUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "knowledge",
					"description": "knowledge",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/KnowledgeInfo",
							"originalRef": "KnowledgeInfo"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«KnowledgeInfo»»",
							"originalRef": "CommonResult«List«KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/build/refreshBoards": {
			"get": {
				"tags": ["/management/build"],
				"summary": "refreshBoards",
				"operationId": "refreshBoardsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/build/refreshCache": {
			"get": {
				"tags": ["/management/build"],
				"summary": "refreshCache",
				"operationId": "refreshCacheUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/build/refreshKnowledge": {
			"get": {
				"tags": ["/management/build"],
				"summary": "refreshKnowledge",
				"operationId": "refreshKnowledgeUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/build/refreshMediaElementCache": {
			"get": {
				"tags": ["/management/build"],
				"summary": "refreshMediaElementCache",
				"operationId": "refreshMediaElementCacheUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/build/refreshProducts": {
			"get": {
				"tags": ["/management/build"],
				"summary": "refreshProducts",
				"operationId": "refreshProductsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/autoSplit": {
			"post": {
				"tags": ["/management/document"],
				"summary": "自动拆分",
				"operationId": "splitDocUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}, {
					"name": "splitType",
					"in": "query",
					"description": "splitType",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/count": {
			"get": {
				"tags": ["/management/document"],
				"summary": "count",
				"operationId": "countUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/deleteKnowledge": {
			"post": {
				"tags": ["/management/document"],
				"summary": "deleteKnowledge",
				"operationId": "deleteKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fileId",
					"in": "query",
					"description": "fileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/download": {
			"post": {
				"tags": ["/management/document"],
				"summary": "download",
				"operationId": "downloadUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ResponseEntity",
							"originalRef": "ResponseEntity"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/eventBus": {
			"get": {
				"tags": ["/management/document"],
				"summary": "eventBus",
				"operationId": "eventBusUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "action",
					"in": "query",
					"description": "action",
					"required": false,
					"type": "string"
				}, {
					"name": "fileId",
					"in": "query",
					"description": "fileId",
					"required": false,
					"type": "string"
				}, {
					"name": "type",
					"in": "query",
					"description": "type",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/getContent": {
			"post": {
				"tags": ["/management/document"],
				"summary": "getContent",
				"operationId": "getContentUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/list": {
			"post": {
				"tags": ["/management/document"],
				"summary": "list",
				"operationId": "listUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/updateDocFileStatus": {
			"post": {
				"tags": ["/management/document"],
				"summary": "设置文件的拆解状态",
				"operationId": "updateDocFileStatusUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}, {
					"name": "status",
					"in": "query",
					"description": "status",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/updateKnowledgeCategoryLevelFromTop": {
			"post": {
				"tags": ["/management/document"],
				"summary": "设置知识目录的group level 和 display level",
				"operationId": "updateKnowledgeCategoryLevelFromTopUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "displayLevel",
					"in": "query",
					"description": "displayLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "groupLevel",
					"in": "query",
					"description": "groupLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "relevant",
					"in": "query",
					"description": "relevant",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "topId",
					"in": "query",
					"description": "topId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/document/updateProductCategoryLevelFromTop": {
			"post": {
				"tags": ["/management/document"],
				"summary": "设置产品目录的group level 和 display level",
				"operationId": "updateProductCategoryLevelFromTopUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "displayLevel",
					"in": "query",
					"description": "displayLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "groupLevel",
					"in": "query",
					"description": "groupLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "topId",
					"in": "query",
					"description": "topId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_board/listByGroup": {
			"get": {
				"tags": ["/management/forum_board"],
				"summary": "listByGroup",
				"operationId": "listByGroupUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_board_document/listForumBoard": {
			"get": {
				"tags": ["/management/forum_board_document"],
				"summary": "list the tree of all forum board",
				"operationId": "listForumBoardUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_board_document/queryForumBoardDocumentDetail": {
			"post": {
				"tags": ["/management/forum_board_document"],
				"summary": "query forum board document detail information by board",
				"operationId": "queryForumBoardDocumentDetailByBoardUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "board",
					"in": "query",
					"description": "board",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_board_document/update": {
			"post": {
				"tags": ["/management/forum_board_document"],
				"summary": "update document",
				"operationId": "updateUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/Map«string,object»",
							"originalRef": "Map«string,object»"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/add": {
			"post": {
				"tags": ["/management/forum_event"],
				"summary": "add",
				"operationId": "addUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "eventDesc",
					"in": "query",
					"description": "eventDesc",
					"required": true,
					"type": "string"
				}, {
					"name": "eventLink",
					"in": "query",
					"description": "eventLink",
					"required": true,
					"type": "string"
				}, {
					"name": "eventPublishTime",
					"in": "query",
					"description": "eventPublishTime",
					"required": true,
					"type": "string"
				}, {
					"name": "eventTitle",
					"in": "query",
					"description": "eventTitle",
					"required": true,
					"type": "string"
				}, {
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/delete": {
			"post": {
				"tags": ["/management/forum_event"],
				"summary": "delete",
				"operationId": "deleteUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/list": {
			"get": {
				"tags": ["/management/forum_event"],
				"summary": "list",
				"operationId": "listUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/listByGroup": {
			"get": {
				"tags": ["/management/forum_event"],
				"summary": "listByGroup",
				"operationId": "listByGroupUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/totalByGroup": {
			"get": {
				"tags": ["/management/forum_event"],
				"summary": "totalByGroup",
				"operationId": "totalByGroupUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_event/update": {
			"post": {
				"tags": ["/management/forum_event"],
				"summary": "update",
				"operationId": "updateUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "eventDesc",
					"in": "query",
					"description": "eventDesc",
					"required": true,
					"type": "string"
				}, {
					"name": "eventLink",
					"in": "query",
					"description": "eventLink",
					"required": true,
					"type": "string"
				}, {
					"name": "eventPublishTime",
					"in": "query",
					"description": "eventPublishTime",
					"required": true,
					"type": "string"
				}, {
					"name": "eventTitle",
					"in": "query",
					"description": "eventTitle",
					"required": true,
					"type": "string"
				}, {
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "id",
					"in": "query",
					"description": "id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/add": {
			"post": {
				"tags": ["/management/forum_mapping"],
				"summary": "add",
				"operationId": "addUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "productCategoryId",
					"in": "query",
					"description": "productCategoryId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/delete": {
			"post": {
				"tags": ["/management/forum_mapping"],
				"summary": "delete",
				"operationId": "deleteUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumProductMappingPO»",
							"originalRef": "CommonResult«ForumProductMappingPO»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/forumCategory": {
			"get": {
				"tags": ["/management/forum_mapping"],
				"summary": "forumCategory",
				"operationId": "forumCategoryUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/list": {
			"get": {
				"tags": ["/management/forum_mapping"],
				"summary": "list",
				"operationId": "listUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumProductMappingPO»",
							"originalRef": "CommonResult«ForumProductMappingPO»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/productCategory": {
			"get": {
				"tags": ["/management/forum_mapping"],
				"summary": "productCategory",
				"operationId": "productCategoryUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/productCategoryInSearch": {
			"get": {
				"tags": ["/management/forum_mapping"],
				"summary": "productCategoryInSearch",
				"operationId": "productCategoryInSearchUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/forum_mapping/update": {
			"post": {
				"tags": ["/management/forum_mapping"],
				"summary": "update",
				"operationId": "updateUsingPOST_2",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "fid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "id",
					"in": "query",
					"description": "id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "productCategoryId",
					"in": "query",
					"description": "productCategoryId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/add": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "add a lot of knowledge",
				"operationId": "saveKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/Map«string,string»",
							"originalRef": "Map«string,string»"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/count": {
			"get": {
				"tags": ["/management/knowledge"],
				"summary": "count",
				"operationId": "countUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/delete": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "delete knowledge by knowledge id",
				"operationId": "deleteUsingPOST_3",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/list": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "list knowledge by page",
				"operationId": "listUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/listAllKnowledgeCategories": {
			"get": {
				"tags": ["/management/knowledge"],
				"summary": "list all knowledge categories",
				"operationId": "listAllCategoriesUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/listByDocFile": {
			"get": {
				"tags": ["/management/knowledge"],
				"summary": "list knowledge by docFile id",
				"operationId": "listByDocFileUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "docFileId",
					"in": "query",
					"description": "docFileId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/saveOrUpdate": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "save or update a lot of knowledge",
				"operationId": "saveOrUpdateKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/Map«string,string»",
							"originalRef": "Map«string,string»"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/update": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "update a lot of knowledge",
				"operationId": "updateKnowledgeUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "array",
						"items": {
							"$ref": "#/definitions/Map«string,string»",
							"originalRef": "Map«string,string»"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge/updateOne": {
			"post": {
				"tags": ["/management/knowledge"],
				"summary": "updateOne",
				"operationId": "updateOneUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge_category/delete": {
			"post": {
				"tags": ["/management/knowledge_category"],
				"summary": "delete knowledge category",
				"operationId": "deleteUsingPOST_2",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge_category/queryAllKnowledgeCategory": {
			"get": {
				"tags": ["/management/knowledge_category"],
				"summary": "query all knowledge category",
				"operationId": "queryAllKnowledgeCategoriesUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge_category/save": {
			"post": {
				"tags": ["/management/knowledge_category"],
				"summary": "insert knowledge category",
				"operationId": "saveUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "categoryName",
					"in": "query",
					"description": "categoryName",
					"required": true,
					"type": "string"
				}, {
					"name": "parentDisplayLevel",
					"in": "query",
					"description": "parentDisplayLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "parentId",
					"in": "query",
					"description": "parentId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "parentLevel",
					"in": "query",
					"description": "parentLevel",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge_category/treeDataOfKnowledgeCategory": {
			"get": {
				"tags": ["/management/knowledge_category"],
				"summary": "treeDataOfKnowledgeCategory",
				"operationId": "treeDataOfKnowledgeCategoryUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/knowledge_category/update": {
			"post": {
				"tags": ["/management/knowledge_category"],
				"summary": "update knowledge category",
				"operationId": "updateUsingPOST_3",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "param",
					"description": "param",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/deleteHistoryQuestion": {
			"get": {
				"tags": ["/management/question_feedback"],
				"summary": "deleteHistoryQuestion",
				"operationId": "deleteHistoryQuestionUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "deleteAll",
					"in": "query",
					"description": "deleteAll",
					"required": false,
					"type": "string"
				}, {
					"name": "questionId",
					"in": "query",
					"description": "questionId",
					"required": false,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«Map«string,string»»»",
							"originalRef": "CommonResult«List«Map«string,string»»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/download": {
			"post": {
				"tags": ["/management/question_feedback"],
				"summary": "download search history",
				"operationId": "downloadAsExcelUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "paramsMap",
					"description": "paramsMap",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/feedback": {
			"post": {
				"tags": ["/management/question_feedback"],
				"summary": "feedback",
				"operationId": "feedbackUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/queryHistoryQuestion": {
			"get": {
				"tags": ["/management/question_feedback"],
				"summary": "get history question for user",
				"operationId": "queryHistoryQuestionUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«Map«string,string»»»",
							"originalRef": "CommonResult«List«Map«string,string»»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/queryModelResults": {
			"post": {
				"tags": ["/management/question_feedback"],
				"summary": "query model results",
				"operationId": "queryModelResultsUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "paramsMap",
					"description": "paramsMap",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map«string,QAModelResultInfo»»",
							"originalRef": "CommonResult«Map«string,QAModelResultInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/question_feedback/querySearchHistory": {
			"post": {
				"tags": ["/management/question_feedback"],
				"summary": "query search history",
				"operationId": "querySearchHistoryUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "paramsMap",
					"description": "paramsMap",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map«string,QAModelResultInfo»»",
							"originalRef": "CommonResult«Map«string,QAModelResultInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/system_feedback/addRedisSetData": {
			"get": {
				"tags": ["/management/system_feedback"],
				"summary": "清空Redis中指定key的数据",
				"operationId": "addRedisSetDataUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "setKey",
					"in": "query",
					"description": "setKey",
					"required": true,
					"type": "string"
				}, {
					"name": "setValue",
					"in": "query",
					"description": "setValue",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/system_feedback/clearRedisSetData": {
			"get": {
				"tags": ["/management/system_feedback"],
				"summary": "清空Redis中指定key的数据",
				"operationId": "clearRedisSetDataUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "setKey",
					"in": "query",
					"description": "setKey",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/system_feedback/querySystemFeedBack": {
			"post": {
				"tags": ["/management/system_feedback"],
				"summary": "query system feedback results",
				"operationId": "queryModelResultsUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "paramsMap",
					"description": "paramsMap",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map«string,SystemDocFeedbackPO»»",
							"originalRef": "CommonResult«Map«string,SystemDocFeedbackPO»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/addGroupForUser": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "add Group For User",
				"operationId": "addGroupForUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "groupId",
					"in": "query",
					"description": "groupId",
					"required": true,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/addUser": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "add user",
				"operationId": "addUserUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "departName",
					"in": "query",
					"description": "departName",
					"required": true,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "8位员工号，sapId",
					"required": true,
					"type": "string"
				}, {
					"name": "userName",
					"in": "query",
					"description": "userName",
					"required": true,
					"type": "string"
				}, {
					"name": "ystId",
					"in": "query",
					"description": "6位一事通号，ystId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/addUserGroup": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "add a UsetGroup",
				"operationId": "addUserGroupUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "groupName",
					"in": "query",
					"description": "群组名称",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/deleteGroupForUser": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "delete Group For User",
				"operationId": "deleteGroupForUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "groupName",
					"in": "query",
					"description": "groupName",
					"required": true,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/deleteUserById": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "delete user By UserId",
				"operationId": "deleteUserByIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "UserId",
					"required": true,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/deleteUserGroupById": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "delete UsetGroup By id",
				"operationId": "deleteUserGroupUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "群组id",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/findAllRole": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "find all role",
				"operationId": "findAllRoleUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/findUserById": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "find user By UserId",
				"operationId": "findUserByIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "id",
					"in": "query",
					"description": "UserId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/findUserTotal": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "find user total",
				"operationId": "findUserTotalUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/getUser": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "getUser",
				"operationId": "getUserUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/listAllUser": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "get all user",
				"operationId": "findAllUserUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageNum",
					"in": "query",
					"description": "当前页码",
					"required": false,
					"type": "string",
					"default": "1"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "每页条数",
					"required": false,
					"type": "string",
					"default": "10"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/listAllUserGroup": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "get all group",
				"operationId": "findAllUserGroupUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/searchUserByUserNameOrSapId": {
			"get": {
				"tags": ["/management/user_docgroup"],
				"summary": "search user By UserName or SapId or YstId",
				"operationId": "searchUserByUserNameOrSapIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "s",
					"in": "query",
					"description": "UserName or SapId or ystId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/setPlateForUser": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "set Plate For User",
				"operationId": "setPlateForUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "plateVo",
					"description": "plateVo",
					"required": true,
					"schema": {
						"$ref": "#/definitions/PlateVo",
						"originalRef": "PlateVo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/testUser": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "测试行外用户刷新",
				"operationId": "testUserUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "allow",
					"in": "query",
					"description": "allow",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/updateUserAccessLimitedForum": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "update user to access limited forum",
				"operationId": "updateUserAccessLimitedForumUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "allow",
					"in": "query",
					"description": "0",
					"required": true,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/updateUserById": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "update User By Id",
				"operationId": "updateUserByIdUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "department",
					"in": "query",
					"description": "department",
					"required": true,
					"type": "string"
				}, {
					"name": "id",
					"in": "query",
					"description": "UserId",
					"required": true,
					"type": "string"
				}, {
					"name": "roleId",
					"in": "query",
					"description": "roleId",
					"required": true,
					"type": "string"
				}, {
					"name": "sapId",
					"in": "query",
					"description": "sapId",
					"required": true,
					"type": "string"
				}, {
					"name": "userName",
					"in": "query",
					"description": "userName",
					"required": true,
					"type": "string"
				}, {
					"name": "ystId",
					"in": "query",
					"description": "ystId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/management/user/updateUserGroup": {
			"post": {
				"tags": ["/management/user_docgroup"],
				"summary": "update UsetGroup",
				"operationId": "updateUserGroupUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "groupName",
					"in": "query",
					"description": "群组名称",
					"required": true,
					"type": "string"
				}, {
					"name": "id",
					"in": "query",
					"description": "群组id",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/media/bindMedia": {
			"post": {
				"tags": ["media-element-controller"],
				"summary": "bindMedia",
				"operationId": "bindMediaUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "elementId",
					"in": "query",
					"description": "elementId",
					"required": true,
					"type": "string"
				}, {
					"name": "elementType",
					"in": "query",
					"description": "elementType",
					"required": true,
					"type": "string"
				}, {
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/addSystemMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "添加系统消息",
				"description": "接口负责人：吴雪亮",
				"operationId": "addSystemMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "content",
					"in": "query",
					"description": "消息内容",
					"required": false,
					"type": "string"
				}, {
					"name": "title",
					"in": "query",
					"description": "消息标题",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/listMailMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "查询所有私信",
				"description": "接口负责人：吴雪亮",
				"operationId": "listMailMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "recipientUserId",
					"in": "query",
					"description": "接受用户",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«MessageMailInfo»»",
							"originalRef": "CommonResult«List«MessageMailInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/maskAllMessageAsRead": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "聚合统计消息状态",
				"description": "接口负责人：吴雪亮",
				"operationId": "markAllMessageAsReadUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "messageType",
					"in": "query",
					"description": "2-评论/回复 4-收藏/点赞 6-关注 8-订阅消息 10-邀请回答 12-文件操作",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 2
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/queryMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "根据用户ID分页获取用户消息",
				"description": "接口负责人：吴雪亮",
				"operationId": "queryRemindMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "createTime",
					"in": "query",
					"description": "最新未读时间,分页请求（pageIndex > 1）的时候将上一次的请求的第一条的create_time传给后端",
					"required": false,
					"type": "string",
					"x-example": "2019-12-20 17:14:21"
				}, {
					"name": "messageType",
					"in": "query",
					"description": "2-评论/回复 4-收藏/点赞 6-关注 8-订阅消息 10-邀请回答 12-文件操作",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 2
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«MessageRemindInfo»»",
							"originalRef": "CommonResult«PaginationInfo«MessageRemindInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/queryMessageAggregation": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "聚合统计消息状态",
				"description": "接口负责人：吴雪亮",
				"operationId": "queryMessageStatusUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«MessageAggregationInfo»»",
							"originalRef": "CommonResult«List«MessageAggregationInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/querySystemMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "根据用户ID分页获取用户消息",
				"description": "接口负责人：吴雪亮",
				"operationId": "querySystemMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 1
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 10
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«MessageRemindInfo»»",
							"originalRef": "CommonResult«PaginationInfo«MessageRemindInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/replyMailMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "回复私信",
				"description": "接口负责人：吴雪亮",
				"operationId": "replyMailMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "content",
					"in": "query",
					"description": "私信内容",
					"required": false,
					"type": "string",
					"x-example": "0"
				}, {
					"name": "dialogueId",
					"in": "query",
					"description": "对话",
					"required": false,
					"type": "string",
					"x-example": "0"
				}, {
					"name": "recipientUserId",
					"in": "query",
					"description": "接受用户",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "senderUserId",
					"in": "query",
					"description": "senderUserId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userId",
					"in": "query",
					"description": "发送用户ID",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/messageV2/sendMailMessage": {
			"get": {
				"tags": ["/messageV2"],
				"summary": "发送私信",
				"description": "接口负责人：吴雪亮",
				"operationId": "sendMailMessageUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "content",
					"in": "query",
					"description": "私信内容",
					"required": false,
					"type": "string"
				}, {
					"name": "recipientUserId",
					"in": "query",
					"description": "接受用户",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "senderUserId",
					"in": "query",
					"description": "senderUserId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userId",
					"in": "query",
					"description": "发送用户ID",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/cancelTraining": {
			"get": {
				"tags": ["/model"],
				"summary": "cancel training model",
				"operationId": "cancelTrainingUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "modelTag",
					"in": "query",
					"description": "modelTag",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«boolean»",
							"originalRef": "CommonResult«boolean»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/findAllAnnotations": {
			"post": {
				"tags": ["/model"],
				"summary": "retrieve all annotations for selecting to train",
				"operationId": "findAllAnnotationsUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "params",
					"description": "params",
					"required": true,
					"schema": {
						"type": "object",
						"additionalProperties": {
							"type": "string"
						}
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«KnowledgeModel»»",
							"originalRef": "CommonResult«PaginationInfo«KnowledgeModel»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/findAllModel": {
			"get": {
				"tags": ["/model"],
				"summary": "find all model",
				"operationId": "findAllModelUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ModelInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ModelInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/findModelDetails": {
			"get": {
				"tags": ["/model"],
				"summary": "find model details info by model tag and show info into page",
				"operationId": "findModelDetailsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "modelTag",
					"in": "query",
					"description": "modelTag",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ModelInfo»»",
							"originalRef": "CommonResult«List«ModelInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/findTrainingModel": {
			"get": {
				"tags": ["/model"],
				"summary": "find training model",
				"operationId": "findTrainingModelUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ModelInfo»",
							"originalRef": "CommonResult«ModelInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/findUsingModel": {
			"get": {
				"tags": ["/model"],
				"summary": "find using model",
				"operationId": "findUsingModelUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ModelInfo»",
							"originalRef": "CommonResult«ModelInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/getAllCompletedModel": {
			"get": {
				"tags": ["/model"],
				"summary": "retrieve all finished training model",
				"operationId": "allCompletedModelUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«string»»",
							"originalRef": "CommonResult«List«string»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/onlinePublish": {
			"get": {
				"tags": ["/model"],
				"summary": "request one online publish for model",
				"operationId": "onlinePublishUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "modelTag",
					"in": "query",
					"description": "modelTag",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«boolean»",
							"originalRef": "CommonResult«boolean»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/model/onlineTraining": {
			"post": {
				"tags": ["/model"],
				"summary": "request one online training for model",
				"operationId": "onlineTrainingUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "modelTrainRequest",
					"description": "modelTrainRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ModelTrainRequest",
						"originalRef": "ModelTrainRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«boolean»",
							"originalRef": "CommonResult«boolean»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/notify/queryKMNotices": {
			"get": {
				"tags": ["/notify"],
				"summary": "返回知识和标注需要审核者审核的数量和，审核者拒接批注的数量",
				"description": "接口负责人：陈玉环",
				"operationId": "queryKMNoticesUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«NotifyInfo»",
							"originalRef": "CommonResult«NotifyInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/openapi/document/find": {
			"post": {
				"tags": ["/openapi/document"],
				"summary": "根据目录的路径获取文档信息",
				"description": "接口负责人：xw80329",
				"operationId": "findUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "path",
					"in": "query",
					"description": "/平台银行/案例库",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«OutPagination«OutDocument»»",
							"originalRef": "CommonResult«OutPagination«OutDocument»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/openapi/document/listCategories": {
			"post": {
				"tags": ["/openapi/document"],
				"summary": "根据目录的路径获取分类信息",
				"description": "接口负责人：xw80329",
				"operationId": "listCategoriesUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "level",
					"in": "query",
					"description": "2",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "listable",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}, {
					"name": "path",
					"in": "query",
					"description": "/平台银行/案例库",
					"required": true,
					"type": "string"
				}, {
					"name": "top",
					"in": "query",
					"description": "3",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "totalCalculable",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«OutProductCategory»»",
							"originalRef": "CommonResult«List«OutProductCategory»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/openapi/document/search": {
			"post": {
				"tags": ["/openapi/document"],
				"summary": "根据目录的路径获取文档信息",
				"description": "接口负责人：xw80329",
				"operationId": "searchUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "highlight",
					"in": "query",
					"description": "Y",
					"required": false,
					"type": "string"
				}, {
					"name": "keywords",
					"in": "query",
					"description": "分行",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "10",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "path",
					"in": "query",
					"description": "/平台银行/案例库",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«OutPagination«OutDocument»»",
							"originalRef": "CommonResult«OutPagination«OutDocument»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/openapi/topic/list": {
			"post": {
				"tags": ["/openapi/topic"],
				"summary": "获取置顶的主题",
				"description": "接口负责人：xw80329",
				"operationId": "listUsingPOST_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "top",
					"in": "query",
					"description": "1",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«OutTopic»»",
							"originalRef": "CommonResult«List«OutTopic»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcLogin",
				"operationId": "pcLoginUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}, {
					"name": "NextAction",
					"in": "query",
					"description": "NextAction",
					"required": false,
					"type": "string"
				}, {
					"name": "flashAttributes",
					"in": "query",
					"required": false,
					"type": "object"
				}, {
					"name": "token",
					"in": "query",
					"description": "token",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/create/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/dashboard/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_1",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_1",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_1",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/discuss/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_2",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_2",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_2",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/countUnReadReplies": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "获取首页悬浮小窗中当前用户所有未读的回复的帖子的数量",
				"description": "接口负责人：陈玉环",
				"operationId": "countUnReadRepliesUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "parameter",
					"in": "query",
					"description": "parameter",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map«string,int»»",
							"originalRef": "CommonResult«Map«string,int»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/getAllMarkUserInfo": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "获取 '@'所有可用用户信息",
				"operationId": "getAllMarkUserInfoUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "nameStr",
					"in": "query",
					"description": "nameStr",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/getFloatPostsByForumId": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "根据当前帖子的板块id获取大板块下的所有悬浮帖/实时帖",
				"operationId": "getFloatPostsByForumIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "forumId",
					"in": "query",
					"description": "43",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«SimpleForumPostInfo»»",
							"originalRef": "CommonResult«List«SimpleForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/getMarkUserInfoByTid": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "获取'@'所需要的用户信息",
				"operationId": "getMarkUserInfoUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "tid",
					"in": "query",
					"description": "tid",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/queryFloatPostByThreadId": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "获取悬浮帖详细信息",
				"description": "接口负责人：陈玉环",
				"operationId": "queryFloatPostByThreadIdUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "isToMe",
					"in": "query",
					"description": "是否@我, isToMe = 1时过滤@我",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "threadId",
					"in": "query",
					"description": "主题帖主题id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumFloat»",
							"originalRef": "CommonResult«ForumFloat»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/queryFloatPosts": {
			"get": {
				"tags": ["/pc/floats"],
				"summary": "分页获取悬浮帖",
				"description": "接口负责人：陈玉环",
				"operationId": "queryFloatPostsUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumFloat»»",
							"originalRef": "CommonResult«List«ForumFloat»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/readAllFloatMessages": {
			"post": {
				"tags": ["/pc/floats"],
				"summary": "标记当前用户的所有关于悬浮帖中未读的回复帖的消息全部为已读",
				"description": "接口负责人：陈玉环",
				"operationId": "readAllFloatMessagesUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "postType",
					"in": "query",
					"description": "postType",
					"required": false,
					"type": "string",
					"default": "FLOAT"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/setPostIsFloat": {
			"post": {
				"tags": ["/pc/floats"],
				"summary": "设置帖子为悬浮帖",
				"description": "接口负责人：陈玉环",
				"operationId": "setPostIsFloatUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "threadId",
					"in": "query",
					"description": "threadId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/floats/unsetPostIsFloat": {
			"post": {
				"tags": ["/pc/floats"],
				"summary": "取消帖子为悬浮帖",
				"description": "接口负责人：陈玉环",
				"operationId": "unsetPostIsFloatUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "threadId",
					"in": "query",
					"description": "threadId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/guide/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_3",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_3",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_3",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_3",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_3",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_3",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_3",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_4",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_4",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_4",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_4",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_4",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_4",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_4",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/addBanner": {
			"post": {
				"tags": ["/pc/home/banner"],
				"summary": "后台新增banner数据",
				"description": "接口负责人：王勇",
				"operationId": "addBannerUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "forumBannerInfo",
					"description": "forumBannerInfo",
					"required": true,
					"schema": {
						"$ref": "#/definitions/ForumBannerInfo",
						"originalRef": "ForumBannerInfo"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumBannerInfo»",
							"originalRef": "CommonResult«ForumBannerInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/bannerUploadMedia": {
			"post": {
				"tags": ["/pc/home/banner"],
				"summary": "后台上传图片到banner",
				"description": "接口负责人：王勇",
				"operationId": "bannerUploadMediaUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "entityId",
					"in": "query",
					"description": "entityId",
					"required": true,
					"type": "string"
				}, {
					"name": "entityType",
					"in": "query",
					"description": "entityType",
					"required": true,
					"type": "string"
				}, {
					"name": "upload",
					"in": "formData",
					"description": "upload",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/deletedBannersAll": {
			"get": {
				"tags": ["/pc/home/banner"],
				"summary": "后台删除banner数据",
				"description": "接口负责人：王勇",
				"operationId": "deletedBannersAllUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/queryListBanner": {
			"get": {
				"tags": ["/pc/home/banner"],
				"summary": "查询banner数据(前端)",
				"description": "接口负责人：王勇",
				"operationId": "queryListBannerUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "size",
					"in": "query",
					"description": "size",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumBannerInfo»",
							"originalRef": "CommonResult«ForumBannerInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/queryListEnabledBanner": {
			"get": {
				"tags": ["/pc/home/banner"],
				"summary": "后台查询Enabled/Disabled的banner数据",
				"description": "接口负责人：王勇",
				"operationId": "queryListEnabledBannerUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "enabled",
					"in": "query",
					"description": "enabled",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ForumBanner»",
							"originalRef": "CommonResult«ForumBanner»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/banner/setEnabledBannerStatus": {
			"get": {
				"tags": ["/pc/home/banner"],
				"summary": "后台设置banner为Enabled/Disabled",
				"description": "接口负责人：王勇",
				"operationId": "setEnabledBannerStatusUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "enableStatus",
					"in": "query",
					"description": "enableStatus",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "id",
					"in": "query",
					"description": "id",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/getImportantFiles": {
			"get": {
				"tags": ["/pc/home"],
				"summary": "getImportantFiles",
				"operationId": "getImportantFilesUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«ImportantFileInfo»",
							"originalRef": "CommonResult«ImportantFileInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/queryEggShellThreads": {
			"get": {
				"tags": ["/pc/home"],
				"summary": "query all eggshell threads",
				"operationId": "queryEggShellThreadsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/home/queryTopOneThreads": {
			"get": {
				"tags": ["/pc/home"],
				"summary": "query TopOneThreads",
				"operationId": "queryTopOneThreadsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/message/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_5",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_5",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_5",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_5",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_5",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_5",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_5",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/cleanNewsData": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "清洗资讯数据",
				"operationId": "cleanNewsDataUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/downloadNews": {
			"get": {
				"tags": ["/pc/news"],
				"summary": "资讯下载（包括附件）",
				"operationId": "downloadFileContentUsingGET_2",
				"produces": ["application/octet-stream"],
				"parameters": [{
					"name": "newsId",
					"in": "query",
					"description": "newsId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/executeJob": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "同步资讯数据",
				"operationId": "executeJobUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/executeLocalFile": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "同步资讯数据",
				"operationId": "executeLocalFileUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/queryNews": {
			"get": {
				"tags": ["/pc/news"],
				"summary": "查询资讯数据",
				"operationId": "queryNewsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "mediaSource",
					"in": "query",
					"description": "来源",
					"required": false,
					"type": "string",
					"x-example": "外汇"
				}, {
					"name": "pageIndexParam",
					"in": "query",
					"description": "分页索引",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSizeParam",
					"in": "query",
					"description": "分页大小",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "policyComments",
					"in": "query",
					"description": "0",
					"required": false,
					"type": "ref",
					"x-example": "0"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«NewsInfo»»",
							"originalRef": "CommonResult«PaginationInfo«NewsInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/queryNewsDetail": {
			"get": {
				"tags": ["/pc/news"],
				"summary": "查询资讯数据",
				"operationId": "queryNewsDetailUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "newsId",
					"in": "query",
					"description": "资讯ID",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«NewsInfo»",
							"originalRef": "CommonResult«NewsInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/querySourceCategory": {
			"get": {
				"tags": ["/pc/news"],
				"summary": "查询资讯来源",
				"operationId": "querySourceCategoryUsingGET",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«string»»",
							"originalRef": "CommonResult«List«string»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/queryTopNews": {
			"get": {
				"tags": ["/pc/news"],
				"summary": "查询首页优先显示的资讯数据",
				"operationId": "queryTopNewsUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "top",
					"in": "query",
					"description": "热门数量",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«NewsInfo»»",
							"originalRef": "CommonResult«List«NewsInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/updateNewsFavorite": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "资讯收藏",
				"operationId": "updateNewsFavoriteUsingPOST",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"parameters": [{
					"in": "body",
					"name": "postFavoriteRequest",
					"description": "postFavoriteRequest",
					"required": true,
					"schema": {
						"$ref": "#/definitions/PostFavoriteRequest",
						"originalRef": "PostFavoriteRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«int»",
							"originalRef": "CommonResult«int»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/uploadNews": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "查询资讯数据",
				"operationId": "uploadNewsUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/uploadNewsAttachment": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "查询资讯数据",
				"operationId": "uploadAttachmentUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}, {
					"name": "newsId",
					"in": "query",
					"description": "newsId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/news/uploadNewsData": {
			"post": {
				"tags": ["/pc/news"],
				"summary": "查询资讯数据",
				"operationId": "uploadNewsDataUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«string»",
							"originalRef": "CommonResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/noticeLarge/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_6",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_6",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_6",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_6",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_6",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_6",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_6",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/old/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_7",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_7",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_7",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_7",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_7",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_7",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_7",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/search": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "PcSearch",
				"operationId": "PcSearchUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/search/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_8",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_8",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_8",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_8",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_8",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_8",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_8",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/pc/user/**": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingGET_9",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"head": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingHEAD_9",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"post": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPOST_9",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"put": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPUT_9",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"delete": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingDELETE_9",
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"options": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingOPTIONS_9",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			},
			"patch": {
				"tags": ["pc-index-controller"],
				"summary": "pcIndex",
				"operationId": "pcIndexUsingPATCH_9",
				"consumes": ["application/json"],
				"produces": ["*/*"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/eventsByProduct": {
			"get": {
				"tags": ["/productV2"],
				"summary": "根据产品id（板块id）获取当前产品及产品子目录中的所有大事件",
				"description": "接口负责人：吴雪亮",
				"operationId": "eventsByProductUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "productId",
					"in": "query",
					"description": "产品Id",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumEventInfo»»",
							"originalRef": "CommonResult«List«ForumEventInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/favoriteByFile": {
			"get": {
				"tags": ["/productV2"],
				"summary": "根据文件id 收藏/取消收藏文件",
				"description": "接口负责人：刘乐乐",
				"operationId": "favoriteByFileUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fid",
					"in": "query",
					"description": "产品id",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "fileId",
					"in": "query",
					"description": "收藏文件Id",
					"required": true,
					"type": "string"
				}, {
					"name": "isFavorite",
					"in": "query",
					"description": "是否收藏， 1是收藏，0是取消收藏",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/filesByProduct": {
			"get": {
				"tags": ["/productV2"],
				"summary": "根据产品id（板块id）获取当前产品及产品子目录中的所有文件名,检索时加上检索的条件",
				"description": "接口负责人：刘乐乐",
				"operationId": "productFilesUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "namePattern",
					"in": "query",
					"description": "搜索文档名称",
					"required": false,
					"type": "string"
				}, {
					"name": "productId",
					"in": "query",
					"description": "产品Id",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«GroupInfo«string,DocumentFileInfo»»»",
							"originalRef": "CommonResult«PaginationInfo«GroupInfo«string,DocumentFileInfo»»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/knowledgeByProduct": {
			"get": {
				"tags": ["/productV2"],
				"summary": "根据产品id（板块id）获取当前产品及产品子目录中的所有知识",
				"description": "接口负责人：陈玉环",
				"operationId": "allKnowledgeByProductUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "productId",
					"in": "query",
					"description": "产品Id",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«GroupKnowledgeInfo»",
							"originalRef": "CommonResult«GroupKnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/productsByFrequent": {
			"get": {
				"tags": ["/productV2"],
				"summary": "返回产品列表",
				"description": "接口负责人：吴雪亮",
				"operationId": "productsByFrequentUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "top",
					"in": "query",
					"description": "top",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumBoardInfo»»",
							"originalRef": "CommonResult«List«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/productV2/productsByGroup": {
			"get": {
				"tags": ["/productV2"],
				"summary": "返回产品列表",
				"description": "接口负责人：刘乐乐",
				"operationId": "productsByGroupUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userIdParam",
					"in": "query",
					"description": "用户ID",
					"required": false,
					"type": "ref"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumBoardInfo»»",
							"originalRef": "CommonResult«List«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search": {
			"get": {
				"tags": ["pc-index-controller"],
				"summary": "Search",
				"operationId": "SearchUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "Data",
					"in": "query",
					"description": "Data",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ModelAndView",
							"originalRef": "ModelAndView"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/getKnowledgeByIdAndKcId": {
			"get": {
				"tags": ["/search"],
				"summary": "/getKnowledgeByIdAndKcId",
				"operationId": "getKnowledgeByIdAndKcIdUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "knowledgeCategoryId",
					"in": "query",
					"description": "knowledgeCategoryId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "pageIndex",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "pageSize",
					"required": true,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«GroupInfo«int,KnowledgeInfo»»",
							"originalRef": "CommonResult«GroupInfo«int,KnowledgeInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/getSuggestions": {
			"post": {
				"tags": ["/search"],
				"summary": "query suggest words",
				"operationId": "getSuggestionsUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/SuggestionRequest",
						"originalRef": "SuggestionRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«SuggestionInfo»",
							"originalRef": "CommonResult«SuggestionInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/query": {
			"post": {
				"tags": ["/search"],
				"summary": "query knowledge by given questionStr",
				"operationId": "queryUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "request",
					"required": true,
					"schema": {
						"$ref": "#/definitions/QuestionRequest",
						"originalRef": "QuestionRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«QueryResponseInfo»",
							"originalRef": "CommonResult«QueryResponseInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/queryAllKnowledgeCategory": {
			"get": {
				"tags": ["/search"],
				"summary": "query all knowledge category",
				"operationId": "queryAllKnowledgeCategoryUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«GroupInfo«int,KnowledgeCategoryInfo»»»",
							"originalRef": "CommonResult«List«GroupInfo«int,KnowledgeCategoryInfo»»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/queryRelativeKnowledge": {
			"get": {
				"tags": ["/search"],
				"summary": "/queryRelativeKnowledge",
				"operationId": "getAllProdKnowledgeByKnowledgeIdUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadForum": {
			"get": {
				"tags": ["/search"],
				"summary": "(For Test) reload ES data",
				"operationId": "reloadForumUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadForumMapping": {
			"get": {
				"tags": ["/search"],
				"summary": "Reload ES forum mapping",
				"operationId": "reloadForumMappingUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadKnowledge": {
			"get": {
				"tags": ["/search"],
				"summary": "(For Test) reload ES data",
				"operationId": "reloadKnowledgeUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadKnowledgeMapping": {
			"get": {
				"tags": ["/search"],
				"summary": "Reload ES knowledge mapping",
				"operationId": "reloadKnowledgeMappingUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadSuggestion": {
			"get": {
				"tags": ["/search"],
				"summary": "Reload ES suggestion data",
				"operationId": "reloadSuggestionUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/search/reloadSuggestionMapping": {
			"get": {
				"tags": ["/search"],
				"summary": "Reload ES suggestion mapping",
				"operationId": "reloadSuggestionMappingUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«Map»",
							"originalRef": "CommonResult«Map»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/searchV2/addSearchDetailFeedback": {
			"get": {
				"tags": ["/searchV2"],
				"summary": "搜索详情反馈",
				"description": "接口负责人：吴雪亮",
				"operationId": "addSearchFeedbackUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "entityId",
					"in": "query",
					"description": "实体ID",
					"required": false,
					"type": "string",
					"x-example": "1"
				}, {
					"name": "feedbackComments",
					"in": "query",
					"description": "注释",
					"required": false,
					"type": "string",
					"x-example": "不好、排序不对"
				}, {
					"name": "type",
					"in": "query",
					"description": "实体类型",
					"required": false,
					"type": "string",
					"x-example": "post,knowledge",
					"enum": ["DOC_FILE", "POST", "POST_EXPERIENCE", "POST_POLL", "POST_INQUIRY", "MULTI_POST", "USER", "SYSTEM", "KNOWLEDGE", "ANNOTATION", "SEARCH_KEYWORD", "PRODUCT_LINK"]
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/searchV2/addSearchFeedback": {
			"get": {
				"tags": ["/searchV2"],
				"summary": "用户反馈",
				"description": "接口负责人：吴雪亮",
				"operationId": "addSearchFeedbackUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "feedbackComments",
					"in": "query",
					"description": "注释",
					"required": false,
					"type": "string",
					"x-example": "不好、排序不对"
				}, {
					"name": "keywords",
					"in": "query",
					"description": "用户输入的关键词",
					"required": false,
					"type": "string",
					"x-example": "0"
				}, {
					"name": "level",
					"in": "query",
					"description": "评级",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 1
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/searchV2/postFilterOptions": {
			"post": {
				"tags": ["/searchV2"],
				"summary": "根据当前查询条件，返回各个后筛选字段的选项值",
				"operationId": "postFilterOptionsUsingPOST",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "搜索的条件",
					"required": true,
					"schema": {
						"$ref": "#/definitions/SearchRequest",
						"originalRef": "SearchRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/searchV2/query": {
			"post": {
				"tags": ["/searchV2"],
				"summary": "新检索接口",
				"description": "接口负责人：陈玉环",
				"operationId": "queryUsingPOST_1",
				"consumes": ["application/json"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"in": "body",
					"name": "request",
					"description": "检索时的请求参数，包括检索词和过滤条件",
					"required": true,
					"schema": {
						"$ref": "#/definitions/SearchRequest",
						"originalRef": "SearchRequest"
					}
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«SearchResponseInfo»",
							"originalRef": "CommonResult«SearchResponseInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/searchV2/queryKnowledgeById": {
			"get": {
				"tags": ["/searchV2"],
				"summary": "通过知识Id查看知识的详情",
				"description": "接口负责人：陈玉环",
				"operationId": "queryKnowledgeByIdUsingGET_1",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«KnowledgeInfo»",
							"originalRef": "CommonResult«KnowledgeInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/uploadMedia": {
			"post": {
				"tags": ["media-controller"],
				"summary": "uploadMedia",
				"operationId": "uploadMediaUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "knowledgeId",
					"in": "query",
					"description": "knowledgeId",
					"required": true,
					"type": "string"
				}, {
					"name": "mediaType",
					"in": "query",
					"description": "mediaType",
					"required": true,
					"type": "string"
				}, {
					"name": "upload",
					"in": "formData",
					"description": "upload",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/ZkUploadResult«string»",
							"originalRef": "ZkUploadResult«string»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/uploadMedia2": {
			"post": {
				"tags": ["media-controller"],
				"summary": "上传图片功能",
				"description": "接口负责人：陈玉环",
				"operationId": "uploadMedia2UsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "upload",
					"in": "formData",
					"description": "upload",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/uploadVideo": {
			"post": {
				"tags": ["media-controller"],
				"summary": "uploadFile",
				"operationId": "uploadFileUsingPOST_1",
				"consumes": ["multipart/form-data"],
				"produces": ["*/*"],
				"parameters": [{
					"name": "file",
					"in": "formData",
					"description": "file",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/changeUserImage": {
			"post": {
				"tags": ["/userV2"],
				"summary": "更换当前用户自己的头像",
				"description": "接口负责人：陈玉环",
				"operationId": "changeUserImageUsingPOST",
				"consumes": ["multipart/form-data"],
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": true,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "userImage",
					"in": "formData",
					"description": "userImage",
					"required": true,
					"type": "file"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/clearUserHistoryForums": {
			"get": {
				"tags": ["/userV2"],
				"summary": "清除当前用户的历史浏览帖子记录",
				"description": "接口负责人：陈玉环",
				"operationId": "clearUserHistoryForumsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "ref",
					"x-example": "0"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«boolean»",
							"originalRef": "CommonResult«boolean»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/followBoards": {
			"get": {
				"tags": ["/userV2"],
				"summary": "对‘我的页面’关注板块，关注板块和取消关注",
				"operationId": "myFollowBoardsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "fids",
					"in": "query",
					"description": "fids",
					"required": true,
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					},
					"collectionFormat": "multi"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«ForumBoardInfo»»",
							"originalRef": "CommonResult«List«ForumBoardInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/followUser": {
			"get": {
				"tags": ["/userV2"],
				"summary": "关注/取关其他用户",
				"description": "接口负责人：刘乐乐",
				"operationId": "followUserUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "followId",
					"in": "query",
					"description": "被关注/取关人Id",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "isFollow",
					"in": "query",
					"description": "1关注/0取关",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/getBeFollowedUsers": {
			"get": {
				"tags": ["/userV2"],
				"summary": "获取用户的粉丝列表",
				"description": "接口负责人：刘乐乐",
				"operationId": "getBeFollowedUsersUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "enrich",
					"in": "query",
					"description": "是否丰富0/1",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 1
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«List«FansInfo»»",
							"originalRef": "CommonResult«List«FansInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/getFollowedUsers": {
			"get": {
				"tags": ["/userV2"],
				"summary": "用戶关注的用户列表",
				"description": "接口负责人：刘乐乐",
				"operationId": "getFollowedUsersUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "enrich",
					"in": "query",
					"description": "是否丰富0/1",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/initUserPage": {
			"get": {
				"tags": ["/userV2"],
				"summary": "'我的'首頁接口數據",
				"description": "接口负责人：陈玉环",
				"operationId": "completedUserInfoUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«UserInfo»",
							"originalRef": "CommonResult«UserInfo»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/queryFavoritesOfUser": {
			"get": {
				"tags": ["/userV2"],
				"summary": "‘我的收藏数’",
				"description": "接口负责人：刘乐乐",
				"operationId": "queryFavoriteCountOfUserUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "userId",
					"in": "query",
					"description": "用户id",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/queryLikesOfUser": {
			"get": {
				"tags": ["/userV2"],
				"summary": "根据用户ID分页获取用户点过赞的帖子的详细信息",
				"description": "接口负责人：刘乐乐",
				"operationId": "queryLikesOfUserUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/userFavorites": {
			"get": {
				"tags": ["/userV2"],
				"summary": "根据用户ID和收藏类型分页获取'我的收藏'信息",
				"description": "接口负责人：刘乐乐",
				"operationId": "userFavoritesUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "favoriteType",
					"in": "query",
					"description": "收藏类型，收藏类型包括文档，主题帖，回复或者评论帖",
					"required": false,
					"type": "string"
				}, {
					"name": "forumType",
					"in": "query",
					"description": "帖子类型，帖子类型包括分享帖，提问帖，投票贴，所有帖",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "isPolicy",
					"in": "query",
					"description": "政策解读(评论与回答时传1，默认0)",
					"required": false,
					"type": "integer",
					"format": "int32"
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/userHistoryForums": {
			"get": {
				"tags": ["/userV2"],
				"summary": "根据用户ID分页获取用户浏览过的帖子的详细信息",
				"description": "接口负责人：陈玉环",
				"operationId": "userHistoryForumsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": false,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/userPostForums": {
			"get": {
				"tags": ["/userV2"],
				"summary": "根据用户ID和帖子类型分页获取'我的发布'信息",
				"description": "接口负责人：刘乐乐",
				"operationId": "userPostForumsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "forumType",
					"in": "query",
					"description": "帖子类型，帖子类型包括分享帖（8），提问帖（0），投票贴（1），政策解读(9)，回答(10)",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id,userId为null获取当登录用户信息，不为null获取该用户信息",
					"required": false,
					"type": "integer",
					"format": "int32"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult",
							"originalRef": "CommonResult"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/userV2/userReplayForums": {
			"get": {
				"tags": ["/userV2"],
				"summary": "根据用户ID和帖子类型分页获取用户参与的帖子的详细信息",
				"description": "接口负责人：陈玉环",
				"operationId": "userReplayForumsUsingGET",
				"produces": ["application/json;charset=UTF-8"],
				"parameters": [{
					"name": "forumType",
					"in": "query",
					"description": "帖子类型，帖子类型包括分享帖(8)/提问帖(0)，投票贴(1)， 所有帖子的回复帖（999）",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageIndex",
					"in": "query",
					"description": "分页index",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "pageSize",
					"in": "query",
					"description": "分页size",
					"required": true,
					"type": "integer",
					"format": "int32",
					"x-example": 0
				}, {
					"name": "userId",
					"in": "query",
					"description": "用戶Id",
					"required": true,
					"type": "string",
					"x-example": "0"
				}],
				"responses": {
					"200": {
						"description": "OK",
						"schema": {
							"$ref": "#/definitions/CommonResult«PaginationInfo«ForumPostInfo»»",
							"originalRef": "CommonResult«PaginationInfo«ForumPostInfo»»"
						}
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/ws/to_all": {
			"get": {
				"tags": ["/ws"],
				"summary": "toAll",
				"operationId": "toAllUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "channel",
					"in": "query",
					"description": "channel",
					"required": false,
					"type": "string"
				}, {
					"name": "content",
					"in": "query",
					"description": "content",
					"required": false,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		},
		"/ws/to_one": {
			"get": {
				"tags": ["/ws"],
				"summary": "toOne",
				"operationId": "toOneUsingGET",
				"produces": ["*/*"],
				"parameters": [{
					"name": "content",
					"in": "query",
					"description": "content",
					"required": false,
					"type": "string"
				}, {
					"name": "userId",
					"in": "query",
					"description": "userId",
					"required": false,
					"type": "string"
				}],
				"responses": {
					"200": {
						"description": "OK"
					}
				},
				"security": [{
					"x-Auth-Token": ["global"]
				}],
				"deprecated": false
			}
		}
	},
	"securityDefinitions": {
		"x-Auth-Token": {
			"type": "apiKey",
			"name": "x-Auth-Token",
			"in": "header"
		}
	},
	"definitions": {
		"Aggregation": {
			"type": "object",
			"properties": {
				"allAttention": {
					"type": "integer",
					"format": "int32"
				},
				"allMyPolicy": {
					"type": "integer",
					"format": "int32"
				},
				"allPostNumber": {
					"type": "integer",
					"format": "int32"
				},
				"beFollowedUserCount": {
					"type": "integer",
					"format": "int32"
				},
				"byReading": {
					"type": "integer",
					"format": "int32"
				},
				"credit": {
					"type": "integer",
					"format": "int32"
				},
				"experienceForumCount": {
					"type": "integer",
					"format": "int32"
				},
				"followedBoardCount": {
					"type": "integer",
					"format": "int32"
				},
				"followedUserCount": {
					"type": "integer",
					"format": "int32"
				},
				"hasFollowedUserAction": {
					"type": "boolean"
				},
				"hasNewFans": {
					"type": "boolean"
				},
				"inquiryAnswers": {
					"type": "integer",
					"format": "int32"
				},
				"inquiryForumCount": {
					"type": "integer",
					"format": "int32"
				},
				"messageCount": {
					"type": "integer",
					"format": "int32"
				},
				"pollForumCount": {
					"type": "integer",
					"format": "int32"
				},
				"replayForumCount": {
					"type": "integer",
					"format": "int32"
				},
				"wonPraise": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "Aggregation"
		},
		"Annotation": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int32"
				},
				"answerId": {
					"type": "integer",
					"format": "int32"
				},
				"knowledgeLine": {
					"type": "integer",
					"format": "int32"
				},
				"lineContextLength": {
					"type": "integer",
					"format": "int32"
				},
				"lineStart": {
					"type": "integer",
					"format": "int32"
				},
				"text": {
					"type": "string"
				}
			},
			"title": "Annotation"
		},
		"AnnotationContext": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int32"
				},
				"annotations": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/Annotation",
						"originalRef": "Annotation"
					}
				},
				"approverId": {
					"type": "integer",
					"format": "int32"
				},
				"auditTime": {
					"type": "string",
					"format": "date-time"
				},
				"comment": {
					"type": "string"
				},
				"createdBy": {
					"type": "string"
				},
				"createdTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"emptyOfAnnotation": {
					"type": "boolean"
				},
				"emptyOfQuestion": {
					"type": "boolean"
				},
				"fileName": {
					"type": "string"
				},
				"lastModelTag": {
					"type": "string"
				},
				"lastUpdatedBy": {
					"type": "string"
				},
				"lastUpdatedTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"questions": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/Question",
						"originalRef": "Question"
					}
				},
				"source": {
					"type": "string"
				},
				"sourceId": {
					"type": "string"
				},
				"sourceType": {
					"type": "string"
				},
				"status": {
					"type": "string",
					"enum": ["EDITING", "WAITAUDIT", "UNAPPROVE", "AVAILABLE", "DELETED", "COPY_FROM"]
				},
				"suggestion": {
					"type": "string"
				}
			},
			"title": "AnnotationContext"
		},
		"AnnotationContextInfo": {
			"type": "object",
			"properties": {
				"annotations": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AnnotationInfo",
						"originalRef": "AnnotationInfo"
					}
				},
				"approver": {
					"type": "string"
				},
				"approverId": {
					"type": "integer",
					"format": "int32"
				},
				"auditTime": {
					"type": "string",
					"format": "date-time"
				},
				"comment": {
					"type": "string"
				},
				"createdBy": {
					"type": "string"
				},
				"displayStatus": {
					"type": "string"
				},
				"fileName": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"knowledgeId": {
					"type": "string"
				},
				"lastUpdatedBy": {
					"type": "string"
				},
				"lastUpdatedTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"questions": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/QuestionInfo",
						"originalRef": "QuestionInfo"
					}
				},
				"source": {
					"type": "string"
				},
				"sourceType": {
					"type": "string"
				},
				"status": {
					"type": "string"
				},
				"suggestion": {
					"type": "string"
				}
			},
			"title": "AnnotationContextInfo"
		},
		"AnnotationInfo": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int32"
				},
				"answerId": {
					"type": "integer",
					"format": "int32"
				},
				"knowledgeLine": {
					"type": "integer",
					"format": "int32"
				},
				"lineContextLength": {
					"type": "integer",
					"format": "int32"
				},
				"lineStart": {
					"type": "integer",
					"format": "int32"
				},
				"text": {
					"type": "string"
				}
			},
			"title": "AnnotationInfo"
		},
		"AttachMentInfo": {
			"type": "object",
			"properties": {
				"attachMentId": {
					"type": "integer",
					"format": "int32"
				},
				"dateLine": {
					"type": "integer",
					"format": "int64"
				},
				"downLoadName": {
					"type": "string"
				},
				"fileName": {
					"type": "string"
				},
				"fileType": {
					"type": "string"
				},
				"pdfName": {
					"type": "string"
				}
			},
			"title": "AttachMentInfo"
		},
		"BadgeInfo": {
			"type": "object",
			"properties": {
				"badgeCount": {
					"type": "integer",
					"format": "int32"
				},
				"color": {
					"type": "string"
				}
			},
			"title": "BadgeInfo"
		},
		"CategoryInfo": {
			"type": "object",
			"properties": {
				"id": {
					"type": "string"
				},
				"name": {
					"type": "string"
				}
			},
			"title": "CategoryInfo"
		},
		"CommonResult": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "object",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult"
		},
		"CommonResult«AnnotationContextInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/AnnotationContextInfo",
					"originalRef": "AnnotationContextInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«AnnotationContextInfo»"
		},
		"CommonResult«AnnotationContext»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/AnnotationContext",
					"originalRef": "AnnotationContext"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«AnnotationContext»"
		},
		"CommonResult«ForumBannerInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumBannerInfo",
					"originalRef": "ForumBannerInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumBannerInfo»"
		},
		"CommonResult«ForumBanner»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumBanner",
					"originalRef": "ForumBanner"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumBanner»"
		},
		"CommonResult«ForumBoardDetailInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumBoardDetailInfo",
					"originalRef": "ForumBoardDetailInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumBoardDetailInfo»"
		},
		"CommonResult«ForumFloat»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumFloat",
					"originalRef": "ForumFloat"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumFloat»"
		},
		"CommonResult«ForumPollVo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumPollVo",
					"originalRef": "ForumPollVo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumPollVo»"
		},
		"CommonResult«ForumPostInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumPostInfo",
					"originalRef": "ForumPostInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumPostInfo»"
		},
		"CommonResult«ForumPostReplayInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumPostReplayInfo",
					"originalRef": "ForumPostReplayInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumPostReplayInfo»"
		},
		"CommonResult«ForumProductMappingPO»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumProductMappingPO",
					"originalRef": "ForumProductMappingPO"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumProductMappingPO»"
		},
		"CommonResult«ForumQAFileConnectionInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumQAFileConnectionInfo",
					"originalRef": "ForumQAFileConnectionInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumQAFileConnectionInfo»"
		},
		"CommonResult«ForumTagInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ForumTagInfo",
					"originalRef": "ForumTagInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ForumTagInfo»"
		},
		"CommonResult«GlobalSiteInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/GlobalSiteInfo",
					"originalRef": "GlobalSiteInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«GlobalSiteInfo»"
		},
		"CommonResult«GroupInfo«int,KnowledgeInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/GroupInfo«int,KnowledgeInfo»",
					"originalRef": "GroupInfo«int,KnowledgeInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«GroupInfo«int,KnowledgeInfo»»"
		},
		"CommonResult«GroupKnowledgeInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/GroupKnowledgeInfo",
					"originalRef": "GroupKnowledgeInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«GroupKnowledgeInfo»"
		},
		"CommonResult«ImportantFileInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ImportantFileInfo",
					"originalRef": "ImportantFileInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ImportantFileInfo»"
		},
		"CommonResult«KnowledgeInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/KnowledgeInfo",
					"originalRef": "KnowledgeInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«KnowledgeInfo»"
		},
		"CommonResult«List«FansInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/FansInfo",
						"originalRef": "FansInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«FansInfo»»"
		},
		"CommonResult«List«FollowedForumBoardInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/FollowedForumBoardInfo",
						"originalRef": "FollowedForumBoardInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«FollowedForumBoardInfo»»"
		},
		"CommonResult«List«ForumBoardInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumBoardInfo»»"
		},
		"CommonResult«List«ForumEventInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumEventInfo",
						"originalRef": "ForumEventInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumEventInfo»»"
		},
		"CommonResult«List«ForumFloat»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumFloat",
						"originalRef": "ForumFloat"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumFloat»»"
		},
		"CommonResult«List«ForumPostInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumPostInfo",
						"originalRef": "ForumPostInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumPostInfo»»"
		},
		"CommonResult«List«ForumTagInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumTagInfo»»"
		},
		"CommonResult«List«ForumVoterInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ForumVoterInfo",
						"originalRef": "ForumVoterInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ForumVoterInfo»»"
		},
		"CommonResult«List«GroupInfo«int,KnowledgeCategoryInfo»»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/GroupInfo«int,KnowledgeCategoryInfo»",
						"originalRef": "GroupInfo«int,KnowledgeCategoryInfo»"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«GroupInfo«int,KnowledgeCategoryInfo»»»"
		},
		"CommonResult«List«KnowledgeInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«KnowledgeInfo»»"
		},
		"CommonResult«List«Map«string,string»»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/Map«string,string»",
						"originalRef": "Map«string,string»"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«Map«string,string»»»"
		},
		"CommonResult«List«MessageAggregationInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/MessageAggregationInfo",
						"originalRef": "MessageAggregationInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«MessageAggregationInfo»»"
		},
		"CommonResult«List«MessageMailInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/MessageMailInfo",
						"originalRef": "MessageMailInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«MessageMailInfo»»"
		},
		"CommonResult«List«ModelInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/ModelInfo",
						"originalRef": "ModelInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«ModelInfo»»"
		},
		"CommonResult«List«NewsInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/NewsInfo",
						"originalRef": "NewsInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«NewsInfo»»"
		},
		"CommonResult«List«OutProductCategory»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/OutProductCategory",
						"originalRef": "OutProductCategory"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«OutProductCategory»»"
		},
		"CommonResult«List«OutTopic»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/OutTopic",
						"originalRef": "OutTopic"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«OutTopic»»"
		},
		"CommonResult«List«SimpleForumPostInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"$ref": "#/definitions/SimpleForumPostInfo",
						"originalRef": "SimpleForumPostInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«SimpleForumPostInfo»»"
		},
		"CommonResult«List«string»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "array",
					"description": "response data body",
					"items": {
						"type": "string"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«List«string»»"
		},
		"CommonResult«Map«string,QAModelResultInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "object",
					"description": "response data body",
					"additionalProperties": {
						"$ref": "#/definitions/QAModelResultInfo",
						"originalRef": "QAModelResultInfo"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«Map«string,QAModelResultInfo»»"
		},
		"CommonResult«Map«string,SystemDocFeedbackPO»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "object",
					"description": "response data body",
					"additionalProperties": {
						"$ref": "#/definitions/SystemDocFeedbackPO",
						"originalRef": "SystemDocFeedbackPO"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«Map«string,SystemDocFeedbackPO»»"
		},
		"CommonResult«Map«string,int»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "object",
					"description": "response data body",
					"additionalProperties": {
						"type": "integer",
						"format": "int32"
					}
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«Map«string,int»»"
		},
		"CommonResult«Map»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "object",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«Map»"
		},
		"CommonResult«ModelInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/ModelInfo",
					"originalRef": "ModelInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«ModelInfo»"
		},
		"CommonResult«NewsInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/NewsInfo",
					"originalRef": "NewsInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«NewsInfo»"
		},
		"CommonResult«NotifyInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/NotifyInfo",
					"originalRef": "NotifyInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«NotifyInfo»"
		},
		"CommonResult«OutPagination«OutDocument»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/OutPagination«OutDocument»",
					"originalRef": "OutPagination«OutDocument»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«OutPagination«OutDocument»»"
		},
		"CommonResult«PaginationInfo«AnnotationContextInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«AnnotationContextInfo»",
					"originalRef": "PaginationInfo«AnnotationContextInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«AnnotationContextInfo»»"
		},
		"CommonResult«PaginationInfo«ForumBoardInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumBoardInfo»",
					"originalRef": "PaginationInfo«ForumBoardInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumBoardInfo»»"
		},
		"CommonResult«PaginationInfo«ForumEventInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumEventInfo»",
					"originalRef": "PaginationInfo«ForumEventInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumEventInfo»»"
		},
		"CommonResult«PaginationInfo«ForumPostInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumPostInfo»»"
		},
		"CommonResult«PaginationInfo«ForumPostReplayInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumPostReplayInfo»",
					"originalRef": "PaginationInfo«ForumPostReplayInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumPostReplayInfo»»"
		},
		"CommonResult«PaginationInfo«ForumQAFileConnectionDTO»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumQAFileConnectionDTO»",
					"originalRef": "PaginationInfo«ForumQAFileConnectionDTO»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumQAFileConnectionDTO»»"
		},
		"CommonResult«PaginationInfo«ForumThreadInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ForumThreadInfo»",
					"originalRef": "PaginationInfo«ForumThreadInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ForumThreadInfo»»"
		},
		"CommonResult«PaginationInfo«GroupInfo«string,DocumentFileInfo»»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«GroupInfo«string,DocumentFileInfo»»",
					"originalRef": "PaginationInfo«GroupInfo«string,DocumentFileInfo»»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«GroupInfo«string,DocumentFileInfo»»»"
		},
		"CommonResult«PaginationInfo«KnowledgeInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«KnowledgeInfo»",
					"originalRef": "PaginationInfo«KnowledgeInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«KnowledgeInfo»»"
		},
		"CommonResult«PaginationInfo«KnowledgeModel»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«KnowledgeModel»",
					"originalRef": "PaginationInfo«KnowledgeModel»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«KnowledgeModel»»"
		},
		"CommonResult«PaginationInfo«MessageRemindInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«MessageRemindInfo»",
					"originalRef": "PaginationInfo«MessageRemindInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«MessageRemindInfo»»"
		},
		"CommonResult«PaginationInfo«ModelInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«ModelInfo»",
					"originalRef": "PaginationInfo«ModelInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«ModelInfo»»"
		},
		"CommonResult«PaginationInfo«NewsInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«NewsInfo»",
					"originalRef": "PaginationInfo«NewsInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«NewsInfo»»"
		},
		"CommonResult«PaginationInfo«NotificationInfo»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«NotificationInfo»",
					"originalRef": "PaginationInfo«NotificationInfo»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«NotificationInfo»»"
		},
		"CommonResult«PaginationInfo«QAUploadRecord»»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/PaginationInfo«QAUploadRecord»",
					"originalRef": "PaginationInfo«QAUploadRecord»"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«PaginationInfo«QAUploadRecord»»"
		},
		"CommonResult«QueryResponseInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/QueryResponseInfo",
					"originalRef": "QueryResponseInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«QueryResponseInfo»"
		},
		"CommonResult«SearchResponseInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/SearchResponseInfo",
					"originalRef": "SearchResponseInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«SearchResponseInfo»"
		},
		"CommonResult«StatisticsChart»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/StatisticsChart",
					"originalRef": "StatisticsChart"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«StatisticsChart»"
		},
		"CommonResult«SuggestionInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/SuggestionInfo",
					"originalRef": "SuggestionInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«SuggestionInfo»"
		},
		"CommonResult«UserInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/UserInfo",
					"originalRef": "UserInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«UserInfo»"
		},
		"CommonResult«UserSiteInfo»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"description": "response data body",
					"$ref": "#/definitions/UserSiteInfo",
					"originalRef": "UserSiteInfo"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«UserSiteInfo»"
		},
		"CommonResult«boolean»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "boolean",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«boolean»"
		},
		"CommonResult«int»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "integer",
					"format": "int32",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«int»"
		},
		"CommonResult«string»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "string",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				}
			},
			"title": "CommonResult«string»"
		},
		"DocumentFileInfo": {
			"type": "object",
			"properties": {
				"badgeInfo": {
					"$ref": "#/definitions/BadgeInfo",
					"originalRef": "BadgeInfo"
				},
				"createdUserName": {
					"type": "string"
				},
				"duplicateByName": {
					"type": "integer",
					"format": "int32"
				},
				"flatHierarchy": {
					"type": "string"
				},
				"group": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"isFavorite": {
					"type": "integer",
					"format": "int32"
				},
				"name": {
					"type": "string"
				},
				"productCategoryId": {
					"type": "string"
				},
				"productCategoryName": {
					"type": "string"
				},
				"status": {
					"type": "string"
				},
				"tags": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"type": {
					"type": "string"
				},
				"uploadDate": {
					"type": "string"
				},
				"url": {
					"type": "string"
				}
			},
			"title": "DocumentFileInfo"
		},
		"FansInfo": {
			"type": "object",
			"properties": {
				"department": {
					"type": "string"
				},
				"fansCount": {
					"type": "integer",
					"format": "int32"
				},
				"isFollow": {
					"type": "integer",
					"format": "int32"
				},
				"isMutual": {
					"type": "integer",
					"format": "int32"
				},
				"postsCount": {
					"type": "integer",
					"format": "int32"
				},
				"replyCount": {
					"type": "integer",
					"format": "int32"
				},
				"userHeaderPortraitId": {
					"type": "string"
				},
				"userHeaderPortraitPath": {
					"type": "string"
				},
				"userId": {
					"type": "string"
				},
				"userName": {
					"type": "string"
				},
				"userTitle": {
					"type": "string"
				}
			},
			"title": "FansInfo"
		},
		"File": {
			"type": "object",
			"properties": {
				"absolute": {
					"type": "boolean"
				},
				"absoluteFile": {
					"$ref": "#/definitions/File",
					"originalRef": "File"
				},
				"absolutePath": {
					"type": "string"
				},
				"canonicalFile": {
					"$ref": "#/definitions/File",
					"originalRef": "File"
				},
				"canonicalPath": {
					"type": "string"
				},
				"directory": {
					"type": "boolean"
				},
				"executable": {
					"type": "boolean"
				},
				"file": {
					"type": "boolean"
				},
				"freeSpace": {
					"type": "integer",
					"format": "int64"
				},
				"hidden": {
					"type": "boolean"
				},
				"lastModified": {
					"type": "integer",
					"format": "int64"
				},
				"name": {
					"type": "string"
				},
				"parent": {
					"type": "string"
				},
				"parentFile": {
					"$ref": "#/definitions/File",
					"originalRef": "File"
				},
				"path": {
					"type": "string"
				},
				"readable": {
					"type": "boolean"
				},
				"totalSpace": {
					"type": "integer",
					"format": "int64"
				},
				"usableSpace": {
					"type": "integer",
					"format": "int64"
				},
				"writable": {
					"type": "boolean"
				}
			},
			"title": "File"
		},
		"FollowedForumBoardInfo": {
			"type": "object",
			"properties": {
				"badgeInfo": {
					"example": [],
					"description": "徽章信息",
					"$ref": "#/definitions/BadgeInfo",
					"originalRef": "BadgeInfo"
				},
				"children": {
					"type": "array",
					"example": [],
					"description": "子版块",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"description": {
					"type": "string"
				},
				"eventFileDisplayable": {
					"type": "integer",
					"format": "int32"
				},
				"followed": {
					"type": "boolean"
				},
				"icon": {
					"type": "string"
				},
				"iconStatus": {
					"type": "object",
					"additionalProperties": {
						"type": "string"
					}
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"leaderBoard": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/UserInfo",
						"originalRef": "UserInfo"
					}
				},
				"moderators": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/UserInfo",
						"originalRef": "UserInfo"
					}
				},
				"prefix": {
					"type": "string"
				},
				"productId": {
					"type": "string"
				},
				"title": {
					"type": "string"
				},
				"type": {
					"type": "string"
				},
				"unReadFileSize": {
					"type": "integer",
					"format": "int32"
				},
				"virtual": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "FollowedForumBoardInfo"
		},
		"ForumBanner": {
			"type": "object",
			"properties": {
				"createdByUserId": {
					"type": "integer",
					"format": "int32"
				},
				"createdByUserName": {
					"type": "string"
				},
				"createdTime": {
					"type": "string",
					"format": "date-time"
				},
				"enabled": {
					"type": "integer",
					"format": "int32"
				},
				"entityId": {
					"type": "string"
				},
				"entityType": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"mediaId": {
					"type": "string"
				},
				"modifiedByUserId": {
					"type": "integer",
					"format": "int32"
				},
				"modifiedByUserName": {
					"type": "string"
				},
				"modifiedTime": {
					"type": "string",
					"format": "date-time"
				}
			},
			"title": "ForumBanner"
		},
		"ForumBannerInfo": {
			"type": "object",
			"properties": {
				"createdTime": {
					"type": "string",
					"format": "date-time"
				},
				"enabled": {
					"type": "integer",
					"format": "int32"
				},
				"entityId": {
					"type": "string"
				},
				"entityType": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"mediaId": {
					"type": "string"
				},
				"mediaUrl": {
					"type": "string"
				}
			},
			"title": "ForumBannerInfo"
		},
		"ForumBoardDetailInfo": {
			"type": "object",
			"properties": {
				"allThread": {
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				},
				"boardEvent": {
					"$ref": "#/definitions/PaginationInfo«ForumEventInfo»",
					"originalRef": "PaginationInfo«ForumEventInfo»"
				},
				"documentFiles": {
					"$ref": "#/definitions/PaginationInfo«GroupInfo«string,DocumentFileInfo»»",
					"originalRef": "PaginationInfo«GroupInfo«string,DocumentFileInfo»»"
				},
				"essentialThread": {
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				},
				"forumBoardInfo": {
					"$ref": "#/definitions/ForumBoardInfo",
					"originalRef": "ForumBoardInfo"
				},
				"hotThread": {
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				},
				"knowledgeCategory": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeCategory",
						"originalRef": "KnowledgeCategory"
					}
				},
				"topThread": {
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				}
			},
			"title": "ForumBoardDetailInfo"
		},
		"ForumBoardInfo": {
			"type": "object",
			"properties": {
				"badgeInfo": {
					"example": [],
					"description": "徽章信息",
					"$ref": "#/definitions/BadgeInfo",
					"originalRef": "BadgeInfo"
				},
				"children": {
					"type": "array",
					"example": [],
					"description": "子版块",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"description": {
					"type": "string"
				},
				"eventFileDisplayable": {
					"type": "integer",
					"format": "int32"
				},
				"followed": {
					"type": "boolean"
				},
				"icon": {
					"type": "string"
				},
				"iconStatus": {
					"type": "object",
					"additionalProperties": {
						"type": "string"
					}
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"prefix": {
					"type": "string"
				},
				"productId": {
					"type": "string"
				},
				"title": {
					"type": "string"
				},
				"type": {
					"type": "string"
				},
				"unReadFileSize": {
					"type": "integer",
					"format": "int32"
				},
				"virtual": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumBoardInfo"
		},
		"ForumEventInfo": {
			"type": "object",
			"properties": {
				"date": {
					"type": "string",
					"format": "date-time"
				},
				"eventDesc": {
					"type": "string"
				},
				"eventLink": {
					"type": "string"
				},
				"eventPublishTime": {
					"type": "string"
				},
				"eventTitle": {
					"type": "string"
				},
				"forumGroupId": {
					"type": "integer",
					"format": "int32"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumEventInfo"
		},
		"ForumFloat": {
			"type": "object",
			"properties": {
				"fid": {
					"type": "integer",
					"format": "int32"
				},
				"fidName": {
					"type": "string"
				},
				"newsId": {
					"type": "integer",
					"format": "int32"
				},
				"postId": {
					"type": "integer",
					"format": "int32"
				},
				"postUserId": {
					"type": "integer",
					"format": "int32"
				},
				"replies": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumReply",
						"originalRef": "ForumReply"
					}
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				},
				"unReadReplyMessages": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumFloat"
		},
		"ForumPollInfo": {
			"type": "object",
			"properties": {
				"isPoll": {
					"type": "integer",
					"format": "int32"
				},
				"number": {
					"type": "integer",
					"format": "int32"
				},
				"optionDetail": {
					"type": "string"
				},
				"percent": {
					"type": "string"
				},
				"polloption": {
					"type": "string"
				},
				"polloptionid": {
					"type": "integer",
					"format": "int32"
				},
				"thumbnail": {
					"type": "string"
				}
			},
			"title": "ForumPollInfo"
		},
		"ForumPollVo": {
			"type": "object",
			"properties": {
				"isPoll": {
					"type": "integer",
					"format": "int32"
				},
				"maxChoices": {
					"type": "integer",
					"format": "int32"
				},
				"multiple": {
					"type": "integer",
					"format": "int32"
				},
				"overt": {
					"type": "integer",
					"format": "int32"
				},
				"pollOptions": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumPollInfo",
						"originalRef": "ForumPollInfo"
					}
				},
				"postDate": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"time": {
					"type": "integer",
					"format": "int32"
				},
				"voters": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumPollVo"
		},
		"ForumPostInfo": {
			"type": "object",
			"properties": {
				"attachments": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AttachMentInfo",
						"originalRef": "AttachMentInfo"
					}
				},
				"author": {
					"type": "string"
				},
				"authorId": {
					"type": "integer",
					"format": "int32"
				},
				"content": {
					"type": "string"
				},
				"date": {
					"type": "string"
				},
				"digest": {
					"type": "integer",
					"format": "int32"
				},
				"estype": {
					"type": "string",
					"enum": ["KNOWLEDGE", "FORUM_POST", "SUGGEST"]
				},
				"expiration": {
					"type": "integer",
					"format": "int32"
				},
				"favTimes": {
					"type": "integer",
					"format": "int32"
				},
				"first": {
					"type": "integer",
					"format": "int32"
				},
				"floats": {
					"type": "integer",
					"format": "int32"
				},
				"forumId": {
					"type": "integer",
					"format": "int32"
				},
				"forumReply": {
					"$ref": "#/definitions/ForumReply",
					"originalRef": "ForumReply"
				},
				"forumTags": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				},
				"hot": {
					"type": "integer",
					"format": "int32"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"image": {
					"type": "string"
				},
				"invisible": {
					"type": "integer",
					"format": "int32"
				},
				"inviteInfo": {
					"$ref": "#/definitions/InviteInfo",
					"originalRef": "InviteInfo"
				},
				"isAttachment": {
					"type": "integer",
					"format": "int32"
				},
				"isEnd": {
					"type": "integer",
					"format": "int32"
				},
				"isFavorite": {
					"type": "integer",
					"format": "int32"
				},
				"isLike": {
					"type": "integer",
					"format": "int32"
				},
				"isPolicy": {
					"type": "integer",
					"format": "int32"
				},
				"isPoll": {
					"type": "integer",
					"format": "int32"
				},
				"lastUpdateDate": {
					"type": "string"
				},
				"likeDate": {
					"type": "string"
				},
				"likeUserTag": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"likes": {
					"type": "integer",
					"format": "int32"
				},
				"matchedTags": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"name": {
					"type": "string"
				},
				"newFeedbackCount": {
					"type": "integer",
					"format": "int32"
				},
				"newsId": {
					"type": "integer",
					"format": "int32"
				},
				"postDate": {
					"type": "string"
				},
				"postType": {
					"type": "string",
					"enum": ["HOT", "NORMAL", "TOP", "ESSENTIAL", "FLOAT"]
				},
				"productCategoryInfo": {
					"$ref": "#/definitions/ProductCategoryInfo",
					"originalRef": "ProductCategoryInfo"
				},
				"replayNumber": {
					"type": "integer",
					"format": "int32"
				},
				"replays": {
					"$ref": "#/definitions/PaginationInfo«ForumPostReplayInfo»",
					"originalRef": "PaginationInfo«ForumPostReplayInfo»"
				},
				"replies": {
					"type": "integer",
					"format": "int32"
				},
				"rid": {
					"type": "integer",
					"format": "int32"
				},
				"special": {
					"type": "integer",
					"format": "int32"
				},
				"text": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				},
				"top": {
					"type": "integer",
					"format": "int32"
				},
				"topModifiedTime": {
					"type": "integer",
					"format": "int32"
				},
				"userInfo": {
					"$ref": "#/definitions/UserInfo",
					"originalRef": "UserInfo"
				},
				"userLastReplyContent": {
					"type": "string"
				},
				"viewDate": {
					"type": "string"
				},
				"views": {
					"type": "integer",
					"format": "int32"
				},
				"voters": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumPostInfo"
		},
		"ForumPostReplayInfo": {
			"type": "object",
			"properties": {
				"attachment": {
					"type": "boolean"
				},
				"author": {
					"type": "string"
				},
				"authorId": {
					"type": "integer",
					"format": "int32"
				},
				"authorInfo": {
					"$ref": "#/definitions/UserInfo",
					"originalRef": "UserInfo"
				},
				"forumReply": {
					"$ref": "#/definitions/ForumReply",
					"originalRef": "ForumReply"
				},
				"image": {
					"type": "string"
				},
				"invisible": {
					"type": "integer",
					"format": "int32"
				},
				"isFirstReplay": {
					"type": "boolean"
				},
				"isLike": {
					"type": "integer",
					"format": "int32"
				},
				"lastUpdateDate": {
					"type": "string"
				},
				"likes": {
					"type": "integer",
					"format": "int32"
				},
				"originalAuthor": {
					"type": "string"
				},
				"originalAuthorId": {
					"type": "integer",
					"format": "int32"
				},
				"pid": {
					"type": "integer",
					"format": "int32"
				},
				"replies": {
					"type": "integer",
					"format": "int32"
				},
				"rid": {
					"type": "integer",
					"format": "int32"
				},
				"text": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				}
			},
			"title": "ForumPostReplayInfo"
		},
		"ForumProductMappingPO": {
			"type": "object",
			"properties": {
				"createdTime": {
					"type": "string",
					"format": "date-time"
				},
				"createdUserId": {
					"type": "string"
				},
				"forumGroupId": {
					"type": "integer",
					"format": "int32"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"modifiedTime": {
					"type": "string",
					"format": "date-time"
				},
				"modifiedUserId": {
					"type": "string"
				},
				"productCategoryId": {
					"type": "string"
				}
			},
			"title": "ForumProductMappingPO"
		},
		"ForumQAFileConnectionDTO": {
			"type": "object",
			"properties": {
				"answer": {
					"type": "string"
				},
				"boardId": {
					"type": "integer",
					"format": "int32"
				},
				"boardName": {
					"type": "string"
				},
				"createTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"createdBy": {
					"type": "string"
				},
				"fileId": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"isDeleted": {
					"type": "integer",
					"format": "int32"
				},
				"lastUpdatedBy": {
					"type": "string"
				},
				"lastUpdatedTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"productCategoryId": {
					"type": "string"
				},
				"question": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumQAFileConnectionDTO"
		},
		"ForumQAFileConnectionInfo": {
			"type": "object",
			"properties": {
				"answer": {
					"type": "string"
				},
				"boardId": {
					"type": "integer",
					"format": "int32"
				},
				"boardName": {
					"type": "string"
				},
				"createTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"createdBy": {
					"type": "string"
				},
				"fileId": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"isDeleted": {
					"type": "integer",
					"format": "int32"
				},
				"lastUpdatedBy": {
					"type": "string"
				},
				"lastUpdatedTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"productCategoryId": {
					"type": "string"
				},
				"question": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumQAFileConnectionInfo"
		},
		"ForumReply": {
			"type": "object",
			"properties": {
				"author": {
					"type": "string"
				},
				"authorId": {
					"type": "integer",
					"format": "int32"
				},
				"favorites": {
					"type": "integer",
					"format": "int32"
				},
				"fid": {
					"type": "integer",
					"format": "int32"
				},
				"isFavorite": {
					"type": "integer",
					"format": "int32"
				},
				"isFirstReply": {
					"type": "integer",
					"format": "int32"
				},
				"isLike": {
					"type": "integer",
					"format": "int32"
				},
				"likes": {
					"type": "integer",
					"format": "int32"
				},
				"message": {
					"type": "string"
				},
				"originalForumReply": {
					"$ref": "#/definitions/ForumReply",
					"originalRef": "ForumReply"
				},
				"pid": {
					"type": "integer",
					"format": "int32"
				},
				"postId": {
					"type": "integer",
					"format": "int32"
				},
				"replayNumber": {
					"type": "integer",
					"format": "int32"
				},
				"replies": {
					"type": "integer",
					"format": "int32"
				},
				"replyId": {
					"type": "integer",
					"format": "int32"
				},
				"replyParentId": {
					"type": "integer",
					"format": "int32"
				},
				"subject": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"updatedTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"userHeaderPortraitPath": {
					"type": "string"
				},
				"userTitle": {
					"type": "string"
				}
			},
			"title": "ForumReply"
		},
		"ForumTagInfo": {
			"type": "object",
			"properties": {
				"createDate": {
					"type": "string",
					"format": "date-time"
				},
				"tagId": {
					"type": "integer",
					"format": "int32"
				},
				"tagName": {
					"type": "string"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				},
				"userName": {
					"type": "string"
				}
			},
			"title": "ForumTagInfo"
		},
		"ForumThreadInfo": {
			"type": "object",
			"properties": {
				"attachments": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AttachMentInfo",
						"originalRef": "AttachMentInfo"
					}
				},
				"author": {
					"type": "string"
				},
				"authorId": {
					"type": "integer",
					"format": "int32"
				},
				"digest": {
					"type": "integer",
					"format": "int32"
				},
				"expiration": {
					"type": "integer",
					"format": "int32"
				},
				"floats": {
					"type": "integer",
					"format": "int32"
				},
				"forumId": {
					"type": "integer",
					"format": "int32"
				},
				"forumTags": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				},
				"hot": {
					"type": "integer",
					"format": "int32"
				},
				"isEnd": {
					"type": "integer",
					"format": "int32"
				},
				"isPoll": {
					"type": "integer",
					"format": "int32"
				},
				"lastUpdateDate": {
					"type": "string"
				},
				"newFeedbackCount": {
					"type": "integer",
					"format": "int32"
				},
				"newsId": {
					"type": "integer",
					"format": "int32"
				},
				"postDate": {
					"type": "string"
				},
				"replies": {
					"type": "integer",
					"format": "int32"
				},
				"special": {
					"type": "integer",
					"format": "int32"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				},
				"top": {
					"type": "integer",
					"format": "int32"
				},
				"userInfo": {
					"$ref": "#/definitions/UserInfo",
					"originalRef": "UserInfo"
				},
				"views": {
					"type": "integer",
					"format": "int32"
				},
				"voters": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ForumThreadInfo"
		},
		"ForumVoterInfo": {
			"type": "object",
			"properties": {
				"polloption": {
					"type": "string"
				},
				"polloptionId": {
					"type": "integer",
					"format": "int32"
				},
				"userNameList": {
					"type": "array",
					"items": {
						"type": "string"
					}
				}
			},
			"title": "ForumVoterInfo"
		},
		"GlobalSiteInfo": {
			"type": "object",
			"properties": {
				"fileDataRestful": {
					"type": "string"
				},
				"forumBoard": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"hotPost": {
					"$ref": "#/definitions/PaginationInfo«ForumPostInfo»",
					"originalRef": "PaginationInfo«ForumPostInfo»"
				}
			},
			"title": "GlobalSiteInfo"
		},
		"GroupInfo": {
			"type": "object",
			"properties": {
				"groupCount": {
					"type": "integer",
					"format": "int32"
				},
				"groupName": {
					"type": "string"
				},
				"groupingData": {
					"type": "array",
					"items": {
						"type": "object"
					}
				},
				"id": {
					"type": "object"
				},
				"name": {
					"type": "string"
				},
				"paginationData": {
					"$ref": "#/definitions/PaginationInfo«object»",
					"originalRef": "PaginationInfo«object»"
				}
			},
			"title": "GroupInfo"
		},
		"GroupInfo«int,KnowledgeCategoryInfo»": {
			"type": "object",
			"properties": {
				"groupCount": {
					"type": "integer",
					"format": "int32"
				},
				"groupName": {
					"type": "string"
				},
				"groupingData": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeCategoryInfo",
						"originalRef": "KnowledgeCategoryInfo"
					}
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"name": {
					"type": "string"
				},
				"paginationData": {
					"$ref": "#/definitions/PaginationInfo«KnowledgeCategoryInfo»",
					"originalRef": "PaginationInfo«KnowledgeCategoryInfo»"
				}
			},
			"title": "GroupInfo«int,KnowledgeCategoryInfo»"
		},
		"GroupInfo«int,KnowledgeInfo»": {
			"type": "object",
			"properties": {
				"groupCount": {
					"type": "integer",
					"format": "int32"
				},
				"groupName": {
					"type": "string"
				},
				"groupingData": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"name": {
					"type": "string"
				},
				"paginationData": {
					"$ref": "#/definitions/PaginationInfo«KnowledgeInfo»",
					"originalRef": "PaginationInfo«KnowledgeInfo»"
				}
			},
			"title": "GroupInfo«int,KnowledgeInfo»"
		},
		"GroupInfo«string,DocumentFileInfo»": {
			"type": "object",
			"properties": {
				"groupCount": {
					"type": "integer",
					"format": "int32"
				},
				"groupName": {
					"type": "string"
				},
				"groupingData": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/DocumentFileInfo",
						"originalRef": "DocumentFileInfo"
					}
				},
				"id": {
					"type": "string"
				},
				"name": {
					"type": "string"
				},
				"paginationData": {
					"$ref": "#/definitions/PaginationInfo«DocumentFileInfo»",
					"originalRef": "PaginationInfo«DocumentFileInfo»"
				}
			},
			"title": "GroupInfo«string,DocumentFileInfo»"
		},
		"GroupKnowledgeInfo": {
			"type": "object",
			"properties": {
				"groupKnowledgeInfo": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/GroupInfo",
						"originalRef": "GroupInfo"
					}
				},
				"knowledgeCategoryInfo": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeCategoryInfo",
						"originalRef": "KnowledgeCategoryInfo"
					}
				},
				"productId": {
					"type": "string"
				},
				"productName": {
					"type": "string"
				}
			},
			"title": "GroupKnowledgeInfo"
		},
		"IdObject": {
			"type": "object",
			"properties": {
				"id": {
					"type": "string"
				},
				"idType": {
					"type": "string"
				}
			},
			"title": "IdObject"
		},
		"ImportantFileInfo": {
			"type": "object",
			"properties": {
				"createDate": {
					"type": "string"
				},
				"docId": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"name": {
					"type": "string"
				},
				"productId": {
					"type": "string"
				},
				"productName": {
					"type": "string"
				},
				"type": {
					"type": "string"
				}
			},
			"title": "ImportantFileInfo"
		},
		"Indicator": {
			"type": "object",
			"properties": {
				"f1": {
					"type": "number",
					"format": "float"
				},
				"precision": {
					"type": "number",
					"format": "float"
				},
				"recall": {
					"type": "number",
					"format": "float"
				}
			},
			"title": "Indicator"
		},
		"InputStream": {
			"type": "object",
			"title": "InputStream"
		},
		"InviteInfo": {
			"type": "object",
			"properties": {
				"inviteSize": {
					"type": "integer",
					"format": "int32"
				},
				"userInfos": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/UserInfo",
						"originalRef": "UserInfo"
					}
				}
			},
			"title": "InviteInfo"
		},
		"InviteRequest": {
			"type": "object",
			"properties": {
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"idType": {
					"type": "string"
				},
				"inviteeUid": {
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					}
				},
				"inviterUid": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "InviteRequest"
		},
		"KnowledgeCategory": {
			"type": "object",
			"properties": {
				"createTime": {
					"$ref": "#/definitions/Timestamp",
					"originalRef": "Timestamp"
				},
				"displayLevel": {
					"type": "integer",
					"format": "int32"
				},
				"enable": {
					"type": "boolean"
				},
				"enabled": {
					"type": "boolean"
				},
				"groupLevel": {
					"type": "integer",
					"format": "int32"
				},
				"hasKnowledge": {
					"type": "boolean"
				},
				"hierarchy": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"level": {
					"type": "integer",
					"format": "int32"
				},
				"name": {
					"type": "string"
				},
				"parentId": {
					"type": "integer",
					"format": "int32"
				},
				"relevant": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "KnowledgeCategory"
		},
		"KnowledgeCategoryInfo": {
			"type": "object",
			"properties": {
				"children": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeCategoryInfo",
						"originalRef": "KnowledgeCategoryInfo"
					}
				},
				"displayLevel": {
					"type": "integer",
					"format": "int32"
				},
				"flatHierarchy": {
					"type": "string"
				},
				"hasKnowledge": {
					"type": "boolean"
				},
				"hidden": {
					"type": "boolean"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"level": {
					"type": "integer",
					"format": "int32"
				},
				"value": {
					"type": "string"
				}
			},
			"title": "KnowledgeCategoryInfo"
		},
		"KnowledgeInfo": {
			"type": "object",
			"properties": {
				"annotationContexts": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AnnotationContextInfo",
						"originalRef": "AnnotationContextInfo"
					}
				},
				"annotationCount": {
					"type": "integer",
					"format": "int32"
				},
				"approver": {
					"type": "string"
				},
				"approverId": {
					"type": "integer",
					"format": "int32"
				},
				"auditTime": {
					"type": "string",
					"format": "date-time"
				},
				"author": {
					"type": "string"
				},
				"comment": {
					"type": "string"
				},
				"content": {
					"type": "string"
				},
				"createUserId": {
					"type": "string"
				},
				"date": {
					"type": "string",
					"format": "date-time"
				},
				"displayOrder": {
					"type": "integer",
					"format": "int32"
				},
				"displayType": {
					"type": "string"
				},
				"docFileId": {
					"type": "string"
				},
				"docFileName": {
					"type": "string"
				},
				"docStatus": {
					"type": "string"
				},
				"estype": {
					"type": "string",
					"enum": ["KNOWLEDGE", "FORUM_POST", "SUGGEST"]
				},
				"htmlContent": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"includingContent": {
					"type": "integer",
					"format": "int32"
				},
				"indexProductCategoryInfo": {
					"$ref": "#/definitions/ProductCategoryInfo",
					"originalRef": "ProductCategoryInfo"
				},
				"keyPhrases": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"keySentences": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"keywords": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"knowledgeCategoryInfo": {
					"$ref": "#/definitions/KnowledgeCategoryInfo",
					"originalRef": "KnowledgeCategoryInfo"
				},
				"knowledgeDisplayStatus": {
					"type": "string"
				},
				"matchedTags": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"modifyUser": {
					"type": "string"
				},
				"modifyUserId": {
					"type": "string"
				},
				"newWords": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NewWord",
						"originalRef": "NewWord"
					}
				},
				"originKnowledgeId": {
					"type": "string"
				},
				"productCategoryInfo": {
					"$ref": "#/definitions/ProductCategoryInfo",
					"originalRef": "ProductCategoryInfo"
				},
				"simpleContent": {
					"type": "boolean"
				},
				"slots": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/Slot",
						"originalRef": "Slot"
					}
				},
				"splitStatusDisplayValue": {
					"type": "string"
				},
				"splitType": {
					"type": "string"
				},
				"status": {
					"type": "string"
				},
				"title": {
					"type": "string"
				}
			},
			"title": "KnowledgeInfo"
		},
		"KnowledgeModel": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int64"
				},
				"fileName": {
					"type": "string"
				},
				"knowledgeCategory": {
					"type": "string"
				},
				"knowledgeId": {
					"type": "string"
				},
				"knowledgeModelId": {
					"type": "integer",
					"format": "int64"
				},
				"knowledgeTitle": {
					"type": "string"
				},
				"modelTag": {
					"type": "string"
				},
				"question": {
					"type": "string"
				}
			},
			"title": "KnowledgeModel"
		},
		"Map«string,QAModelResultInfo»": {
			"type": "object",
			"title": "Map«string,QAModelResultInfo»",
			"additionalProperties": {
				"$ref": "#/definitions/QAModelResultInfo",
				"originalRef": "QAModelResultInfo"
			}
		},
		"Map«string,SystemDocFeedbackPO»": {
			"type": "object",
			"title": "Map«string,SystemDocFeedbackPO»",
			"additionalProperties": {
				"$ref": "#/definitions/SystemDocFeedbackPO",
				"originalRef": "SystemDocFeedbackPO"
			}
		},
		"Map«string,int»": {
			"type": "object",
			"title": "Map«string,int»",
			"additionalProperties": {
				"$ref": "#/definitions/Integer",
				"originalRef": "Integer"
			}
		},
		"Map«string,string»": {
			"type": "object",
			"title": "Map«string,string»",
			"additionalProperties": {
				"type": "string"
			}
		},
		"MedalidInfo": {
			"type": "object",
			"properties": {
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"image": {
					"type": "string"
				},
				"name": {
					"type": "string"
				}
			},
			"title": "MedalidInfo"
		},
		"MessageAggregationInfo": {
			"type": "object",
			"properties": {
				"content": {
					"type": "string"
				},
				"groupName": {
					"type": "string"
				},
				"latestDate": {
					"type": "string"
				},
				"messageType": {
					"type": "integer",
					"format": "int32"
				},
				"unReadCount": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "MessageAggregationInfo"
		},
		"MessageEntity": {
			"type": "object",
			"properties": {
				"author": {
					"type": "string"
				},
				"displayValue": {
					"type": "string"
				},
				"idObjects": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/IdObject",
						"originalRef": "IdObject"
					}
				},
				"title": {
					"type": "string"
				}
			},
			"title": "MessageEntity"
		},
		"MessageMailInfo": {
			"type": "object",
			"properties": {
				"createdTime": {
					"type": "string",
					"format": "date-time"
				},
				"dialogueId": {
					"type": "string"
				},
				"hasRead": {
					"type": "boolean"
				},
				"id": {
					"type": "integer",
					"format": "int64"
				},
				"readTime": {
					"type": "string",
					"format": "date-time"
				},
				"recipientUserId": {
					"type": "integer",
					"format": "int64"
				},
				"senderUserId": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "MessageMailInfo"
		},
		"MessageRemindInfo": {
			"type": "object",
			"properties": {
				"createdTime": {
					"type": "string"
				},
				"entity": {
					"type": "object"
				},
				"entityId": {
					"type": "string"
				},
				"entityObject": {
					"type": "string"
				},
				"entityType": {
					"type": "integer",
					"format": "int64"
				},
				"hasRead": {
					"type": "boolean"
				},
				"id": {
					"type": "integer",
					"format": "int64"
				},
				"messageSource": {
					"type": "string"
				},
				"messageTips": {
					"type": "string"
				},
				"publishType": {
					"type": "string"
				},
				"recipientUserId": {
					"type": "integer",
					"format": "int64"
				},
				"relatedEntity": {
					"$ref": "#/definitions/MessageEntity",
					"originalRef": "MessageEntity"
				},
				"relatedEntityId": {
					"type": "string"
				},
				"senderAction": {
					"type": "string"
				},
				"senderInfo": {
					"$ref": "#/definitions/UserInfo",
					"originalRef": "UserInfo"
				},
				"senderUserId": {
					"type": "integer",
					"format": "int64"
				},
				"senderUserName": {
					"type": "string"
				},
				"tips": {
					"type": "string"
				}
			},
			"title": "MessageRemindInfo"
		},
		"ModelAndView": {
			"type": "object",
			"properties": {
				"empty": {
					"type": "boolean"
				},
				"model": {
					"type": "object"
				},
				"modelMap": {
					"type": "object",
					"additionalProperties": {
						"type": "object"
					}
				},
				"reference": {
					"type": "boolean"
				},
				"status": {
					"type": "string",
					"enum": ["100 CONTINUE", "101 SWITCHING_PROTOCOLS", "102 PROCESSING", "103 CHECKPOINT", "200 OK", "201 CREATED", "202 ACCEPTED", "203 NON_AUTHORITATIVE_INFORMATION", "204 NO_CONTENT", "205 RESET_CONTENT", "206 PARTIAL_CONTENT", "207 MULTI_STATUS", "208 ALREADY_REPORTED", "226 IM_USED", "300 MULTIPLE_CHOICES", "301 MOVED_PERMANENTLY", "302 FOUND", "302 MOVED_TEMPORARILY", "303 SEE_OTHER", "304 NOT_MODIFIED", "305 USE_PROXY", "307 TEMPORARY_REDIRECT", "308 PERMANENT_REDIRECT", "400 BAD_REQUEST", "401 UNAUTHORIZED", "402 PAYMENT_REQUIRED", "403 FORBIDDEN", "404 NOT_FOUND", "405 METHOD_NOT_ALLOWED", "406 NOT_ACCEPTABLE", "407 PROXY_AUTHENTICATION_REQUIRED", "408 REQUEST_TIMEOUT", "409 CONFLICT", "410 GONE", "411 LENGTH_REQUIRED", "412 PRECONDITION_FAILED", "413 PAYLOAD_TOO_LARGE", "413 REQUEST_ENTITY_TOO_LARGE", "414 URI_TOO_LONG", "414 REQUEST_URI_TOO_LONG", "415 UNSUPPORTED_MEDIA_TYPE", "416 REQUESTED_RANGE_NOT_SATISFIABLE", "417 EXPECTATION_FAILED", "418 I_AM_A_TEAPOT", "419 INSUFFICIENT_SPACE_ON_RESOURCE", "420 METHOD_FAILURE", "421 DESTINATION_LOCKED", "422 UNPROCESSABLE_ENTITY", "423 LOCKED", "424 FAILED_DEPENDENCY", "426 UPGRADE_REQUIRED", "428 PRECONDITION_REQUIRED", "429 TOO_MANY_REQUESTS", "431 REQUEST_HEADER_FIELDS_TOO_LARGE", "451 UNAVAILABLE_FOR_LEGAL_REASONS", "500 INTERNAL_SERVER_ERROR", "501 NOT_IMPLEMENTED", "502 BAD_GATEWAY", "503 SERVICE_UNAVAILABLE", "504 GATEWAY_TIMEOUT", "505 HTTP_VERSION_NOT_SUPPORTED", "506 VARIANT_ALSO_NEGOTIATES", "507 INSUFFICIENT_STORAGE", "508 LOOP_DETECTED", "509 BANDWIDTH_LIMIT_EXCEEDED", "510 NOT_EXTENDED", "511 NETWORK_AUTHENTICATION_REQUIRED"]
				},
				"view": {
					"$ref": "#/definitions/View",
					"originalRef": "View"
				},
				"viewName": {
					"type": "string"
				}
			},
			"title": "ModelAndView"
		},
		"ModelInfo": {
			"type": "object",
			"properties": {
				"createBy": {
					"type": "string"
				},
				"createdTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"input": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ModelInputParameter",
						"originalRef": "ModelInputParameter"
					}
				},
				"modelStatus": {
					"type": "string",
					"enum": ["WAITING", "COMPLETED", "FAIL", "TRAINING", "USING", "PUBLISHING", "CANCEL"]
				},
				"modelTag": {
					"type": "string"
				},
				"runMessage": {
					"type": "string"
				},
				"testIndicator": {
					"$ref": "#/definitions/Indicator",
					"originalRef": "Indicator"
				},
				"verifyIndicator": {
					"$ref": "#/definitions/Indicator",
					"originalRef": "Indicator"
				}
			},
			"title": "ModelInfo"
		},
		"ModelInputParameter": {
			"type": "object",
			"properties": {
				"key": {
					"type": "integer",
					"format": "int32"
				},
				"name": {
					"type": "string"
				},
				"type": {
					"type": "string"
				},
				"value": {
					"type": "string"
				}
			},
			"title": "ModelInputParameter"
		},
		"ModelTrainRequest": {
			"type": "object",
			"properties": {
				"inputParameter": {
					"type": "string"
				},
				"knowledgeModels": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeModel",
						"originalRef": "KnowledgeModel"
					}
				},
				"modelTag": {
					"type": "string"
				},
				"selectAll": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ModelTrainRequest"
		},
		"NewPostRequest": {
			"type": "object",
			"properties": {
				"attachMentInfos": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AttachMentInfo",
						"originalRef": "AttachMentInfo"
					}
				},
				"authorId": {
					"type": "integer",
					"format": "int32"
				},
				"boardId": {
					"type": "integer",
					"format": "int32"
				},
				"content": {
					"type": "string"
				},
				"expiration": {
					"type": "integer",
					"format": "int32"
				},
				"forumTagInfo": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumTagInfo",
						"originalRef": "ForumTagInfo"
					}
				},
				"isFloat": {
					"type": "boolean"
				},
				"knowledgeCategoryIds": {
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					}
				},
				"maxChoices": {
					"type": "integer",
					"format": "int32"
				},
				"newsId": {
					"type": "integer",
					"format": "int32"
				},
				"overt": {
					"type": "integer",
					"format": "int32"
				},
				"pollOptions": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/PollOptionInfo",
						"originalRef": "PollOptionInfo"
					}
				},
				"postId": {
					"type": "integer",
					"format": "int32"
				},
				"special": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				}
			},
			"title": "NewPostRequest"
		},
		"NewWord": {
			"type": "object",
			"properties": {
				"score": {
					"type": "number",
					"format": "float"
				},
				"token": {
					"type": "string"
				}
			},
			"title": "NewWord"
		},
		"NewsAttachmentInfo": {
			"type": "object",
			"properties": {
				"createdTime": {
					"type": "string",
					"format": "date-time"
				},
				"downloadName": {
					"type": "string"
				},
				"fileName": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"pdfName": {
					"type": "string"
				}
			},
			"title": "NewsAttachmentInfo"
		},
		"NewsInfo": {
			"type": "object",
			"properties": {
				"attachments": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NewsAttachmentInfo",
						"originalRef": "NewsAttachmentInfo"
					}
				},
				"category": {
					"type": "string"
				},
				"favoriteNum": {
					"type": "integer",
					"format": "int32"
				},
				"hasAttachment": {
					"type": "boolean"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"infoContent": {
					"type": "string"
				},
				"infoPublishDate": {
					"type": "string",
					"format": "date-time"
				},
				"infoTitle": {
					"type": "string"
				},
				"isFavorite": {
					"type": "integer",
					"format": "int32"
				},
				"isForum": {
					"type": "integer",
					"format": "int32"
				},
				"mediaSource": {
					"type": "string"
				},
				"recordInsertTime": {
					"type": "string",
					"format": "date-time"
				},
				"referenceId": {
					"type": "string"
				},
				"replies": {
					"type": "integer",
					"format": "int32"
				},
				"subCategory": {
					"type": "string"
				},
				"subTitle": {
					"type": "string"
				},
				"tid": {
					"type": "integer",
					"format": "int32"
				},
				"updatedTime": {
					"type": "string",
					"format": "date-time"
				}
			},
			"title": "NewsInfo"
		},
		"NotificationInfo": {
			"type": "object",
			"properties": {
				"date": {
					"type": "string"
				},
				"image": {
					"type": "string"
				},
				"message": {
					"type": "string"
				},
				"messageId": {
					"type": "integer",
					"format": "int32"
				},
				"receiver": {
					"type": "integer",
					"format": "int32"
				},
				"sender": {
					"type": "string"
				},
				"special": {
					"type": "integer",
					"format": "int32"
				},
				"status": {
					"type": "integer",
					"format": "int32"
				},
				"text": {
					"type": "string"
				},
				"threadContent": {
					"type": "string"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"threadTitle": {
					"type": "string"
				}
			},
			"title": "NotificationInfo"
		},
		"NotifyInfo": {
			"type": "object",
			"properties": {
				"unReadCommitAnnotationCount": {
					"type": "integer",
					"format": "int32"
				},
				"unReadCommitKnowledgeCount": {
					"type": "integer",
					"format": "int32"
				},
				"unReadRejectAnnotationCount": {
					"type": "integer",
					"format": "int32"
				},
				"unReadRejectKnowledgeCount": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "NotifyInfo"
		},
		"OutDocument": {
			"type": "object",
			"properties": {
				"createdDate": {
					"type": "string",
					"format": "date-time"
				},
				"creator": {
					"$ref": "#/definitions/OutUser",
					"originalRef": "OutUser"
				},
				"detailUrl": {
					"type": "string"
				},
				"docId": {
					"type": "string"
				},
				"lastUpdatedDate": {
					"type": "string",
					"format": "date-time"
				},
				"path": {
					"type": "string"
				},
				"tags": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"title": {
					"type": "string"
				}
			},
			"title": "OutDocument"
		},
		"OutPagination«OutDocument»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/OutDocument",
						"originalRef": "OutDocument"
					}
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "OutPagination«OutDocument»"
		},
		"OutProductCategory": {
			"type": "object",
			"properties": {
				"categoryName": {
					"type": "string"
				},
				"children": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/OutProductCategory",
						"originalRef": "OutProductCategory"
					}
				},
				"docTotalCount": {
					"type": "integer",
					"format": "int32"
				},
				"docs": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/OutDocument",
						"originalRef": "OutDocument"
					}
				},
				"flatHierarchy": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"totalCategory": {
					"type": "boolean"
				}
			},
			"title": "OutProductCategory"
		},
		"OutTopic": {
			"type": "object",
			"properties": {
				"createdDate": {
					"type": "string",
					"format": "date-time"
				},
				"detailUrl": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"img": {
					"type": "string"
				},
				"replyCount": {
					"type": "integer",
					"format": "int32"
				},
				"tags": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"title": {
					"type": "string"
				},
				"topicType": {
					"type": "string"
				},
				"viewCount": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "OutTopic"
		},
		"OutUser": {
			"type": "object",
			"properties": {
				"name": {
					"type": "string"
				},
				"sapId": {
					"type": "string"
				},
				"userId": {
					"type": "string"
				}
			},
			"title": "OutUser"
		},
		"PaginationInfo«AnnotationContextInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AnnotationContextInfo",
						"originalRef": "AnnotationContextInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«AnnotationContextInfo»"
		},
		"PaginationInfo«DocumentFileInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/DocumentFileInfo",
						"originalRef": "DocumentFileInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«DocumentFileInfo»"
		},
		"PaginationInfo«ForumBoardInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumBoardInfo»"
		},
		"PaginationInfo«ForumEventInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumEventInfo",
						"originalRef": "ForumEventInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumEventInfo»"
		},
		"PaginationInfo«ForumPostInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumPostInfo",
						"originalRef": "ForumPostInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumPostInfo»"
		},
		"PaginationInfo«ForumPostReplayInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumPostReplayInfo",
						"originalRef": "ForumPostReplayInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumPostReplayInfo»"
		},
		"PaginationInfo«ForumQAFileConnectionDTO»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumQAFileConnectionDTO",
						"originalRef": "ForumQAFileConnectionDTO"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumQAFileConnectionDTO»"
		},
		"PaginationInfo«ForumThreadInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumThreadInfo",
						"originalRef": "ForumThreadInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ForumThreadInfo»"
		},
		"PaginationInfo«GroupInfo«string,DocumentFileInfo»»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/GroupInfo«string,DocumentFileInfo»",
						"originalRef": "GroupInfo«string,DocumentFileInfo»"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«GroupInfo«string,DocumentFileInfo»»"
		},
		"PaginationInfo«KnowledgeCategoryInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeCategoryInfo",
						"originalRef": "KnowledgeCategoryInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«KnowledgeCategoryInfo»"
		},
		"PaginationInfo«KnowledgeInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeInfo",
						"originalRef": "KnowledgeInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«KnowledgeInfo»"
		},
		"PaginationInfo«KnowledgeModel»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/KnowledgeModel",
						"originalRef": "KnowledgeModel"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«KnowledgeModel»"
		},
		"PaginationInfo«MessageRemindInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/MessageRemindInfo",
						"originalRef": "MessageRemindInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«MessageRemindInfo»"
		},
		"PaginationInfo«ModelInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ModelInfo",
						"originalRef": "ModelInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«ModelInfo»"
		},
		"PaginationInfo«NewsInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NewsInfo",
						"originalRef": "NewsInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«NewsInfo»"
		},
		"PaginationInfo«NotificationInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NotificationInfo",
						"originalRef": "NotificationInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«NotificationInfo»"
		},
		"PaginationInfo«QAUploadRecord»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/QAUploadRecord",
						"originalRef": "QAUploadRecord"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«QAUploadRecord»"
		},
		"PaginationInfo«SearchResultInfo»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/SearchResultInfo",
						"originalRef": "SearchResultInfo"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«SearchResultInfo»"
		},
		"PaginationInfo«object»": {
			"type": "object",
			"properties": {
				"data": {
					"type": "array",
					"items": {
						"type": "object"
					}
				},
				"lazyLoad": {
					"type": "boolean"
				},
				"limit": {
					"type": "integer",
					"format": "int32"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"totalCount": {
					"type": "integer",
					"format": "int64"
				}
			},
			"title": "PaginationInfo«object»"
		},
		"PlateVo": {
			"type": "object",
			"properties": {
				"list": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "PlateVo"
		},
		"PollOptionInfo": {
			"type": "object",
			"properties": {
				"optionDetail": {
					"type": "string"
				},
				"pollOption": {
					"type": "string"
				},
				"thumbnail": {
					"type": "string"
				}
			},
			"title": "PollOptionInfo"
		},
		"PollRequest": {
			"type": "object",
			"properties": {
				"options": {
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					}
				},
				"tid": {
					"type": "integer",
					"format": "int32"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "PollRequest"
		},
		"PostFavoriteRequest": {
			"type": "object",
			"properties": {
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"idType": {
					"type": "string"
				},
				"isFavorite": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "PostFavoriteRequest"
		},
		"PostLikeRequest": {
			"type": "object",
			"properties": {
				"pid": {
					"type": "integer",
					"format": "int32"
				},
				"rid": {
					"type": "integer",
					"format": "int32"
				},
				"tid": {
					"type": "integer",
					"format": "int32"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "PostLikeRequest"
		},
		"ProductCategoryInfo": {
			"type": "object",
			"properties": {
				"children": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ProductCategoryInfo",
						"originalRef": "ProductCategoryInfo"
					}
				},
				"flatHierarchy": {
					"type": "string"
				},
				"hierarchy": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"id": {
					"type": "string"
				},
				"mappingForumId": {
					"type": "integer",
					"format": "int32"
				},
				"value": {
					"type": "string"
				}
			},
			"title": "ProductCategoryInfo"
		},
		"QAModelResultInfo": {
			"type": "object",
			"properties": {
				"matchedQuestion": {
					"type": "string"
				},
				"result": {
					"type": "string"
				},
				"sourceDocumentID": {
					"type": "string"
				},
				"sourceDocumentType": {
					"type": "string"
				},
				"sourceUrl": {
					"type": "string"
				}
			},
			"title": "QAModelResultInfo"
		},
		"QASimilarQuestionInfo": {
			"type": "object",
			"properties": {
				"id": {
					"type": "string"
				},
				"question": {
					"type": "string"
				}
			},
			"title": "QASimilarQuestionInfo"
		},
		"QAUploadRecord": {
			"type": "object",
			"properties": {
				"comment": {
					"type": "string"
				},
				"createTimestamp": {
					"type": "string",
					"format": "date-time"
				},
				"ecsPath": {
					"type": "string"
				},
				"fileName": {
					"type": "string"
				},
				"id": {
					"type": "string"
				},
				"total": {
					"type": "integer",
					"format": "int32"
				},
				"uploadResult": {
					"type": "string"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				},
				"userName": {
					"type": "string"
				}
			},
			"title": "QAUploadRecord"
		},
		"QueryGroupInfo": {
			"type": "object",
			"properties": {
				"groupId": {
					"type": "string"
				},
				"groupName": {
					"type": "string"
				},
				"qaModelResult": {
					"$ref": "#/definitions/QAModelResultInfo",
					"originalRef": "QAModelResultInfo"
				},
				"relevantBoards": {
					"$ref": "#/definitions/PaginationInfo«ForumBoardInfo»",
					"originalRef": "PaginationInfo«ForumBoardInfo»"
				},
				"relevantQuestions": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/QASimilarQuestionInfo",
						"originalRef": "QASimilarQuestionInfo"
					}
				},
				"searchResult": {
					"$ref": "#/definitions/PaginationInfo«SearchResultInfo»",
					"originalRef": "PaginationInfo«SearchResultInfo»"
				}
			},
			"title": "QueryGroupInfo"
		},
		"QueryResponseInfo": {
			"type": "object",
			"properties": {
				"questionId": {
					"type": "string"
				},
				"resultGroup": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/QueryGroupInfo",
						"originalRef": "QueryGroupInfo"
					}
				}
			},
			"title": "QueryResponseInfo"
		},
		"Question": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int32"
				},
				"question": {
					"type": "string"
				},
				"questionId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "Question"
		},
		"QuestionInfo": {
			"type": "object",
			"properties": {
				"annotationId": {
					"type": "integer",
					"format": "int32"
				},
				"question": {
					"type": "string"
				},
				"questionId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "QuestionInfo"
		},
		"QuestionRequest": {
			"type": "object",
			"properties": {
				"knowledgeCategoryIds": {
					"type": "array",
					"items": {
						"type": "integer",
						"format": "int32"
					}
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"productCategoryId": {
					"type": "string"
				},
				"questionId": {
					"type": "string"
				},
				"questionStr": {
					"type": "string"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "QuestionRequest"
		},
		"ReplayRequest": {
			"type": "object",
			"properties": {
				"attachMentInfos": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/AttachMentInfo",
						"originalRef": "AttachMentInfo"
					}
				},
				"content": {
					"type": "string"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32"
				},
				"policy": {
					"type": "integer",
					"format": "int32"
				},
				"postId": {
					"type": "integer",
					"format": "int32"
				},
				"postUserId": {
					"type": "integer",
					"format": "int32"
				},
				"rid": {
					"type": "integer",
					"format": "int32"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"userId": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ReplayRequest"
		},
		"Resource": {
			"type": "object",
			"properties": {
				"description": {
					"type": "string"
				},
				"file": {
					"$ref": "#/definitions/File",
					"originalRef": "File"
				},
				"filename": {
					"type": "string"
				},
				"inputStream": {
					"$ref": "#/definitions/InputStream",
					"originalRef": "InputStream"
				},
				"open": {
					"type": "boolean"
				},
				"readable": {
					"type": "boolean"
				},
				"uri": {
					"$ref": "#/definitions/URI",
					"originalRef": "URI"
				},
				"url": {
					"$ref": "#/definitions/URL",
					"originalRef": "URL"
				}
			},
			"title": "Resource"
		},
		"ResponseEntity": {
			"type": "object",
			"properties": {
				"body": {
					"type": "object"
				},
				"statusCode": {
					"type": "string",
					"enum": ["100 CONTINUE", "101 SWITCHING_PROTOCOLS", "102 PROCESSING", "103 CHECKPOINT", "200 OK", "201 CREATED", "202 ACCEPTED", "203 NON_AUTHORITATIVE_INFORMATION", "204 NO_CONTENT", "205 RESET_CONTENT", "206 PARTIAL_CONTENT", "207 MULTI_STATUS", "208 ALREADY_REPORTED", "226 IM_USED", "300 MULTIPLE_CHOICES", "301 MOVED_PERMANENTLY", "302 FOUND", "302 MOVED_TEMPORARILY", "303 SEE_OTHER", "304 NOT_MODIFIED", "305 USE_PROXY", "307 TEMPORARY_REDIRECT", "308 PERMANENT_REDIRECT", "400 BAD_REQUEST", "401 UNAUTHORIZED", "402 PAYMENT_REQUIRED", "403 FORBIDDEN", "404 NOT_FOUND", "405 METHOD_NOT_ALLOWED", "406 NOT_ACCEPTABLE", "407 PROXY_AUTHENTICATION_REQUIRED", "408 REQUEST_TIMEOUT", "409 CONFLICT", "410 GONE", "411 LENGTH_REQUIRED", "412 PRECONDITION_FAILED", "413 PAYLOAD_TOO_LARGE", "413 REQUEST_ENTITY_TOO_LARGE", "414 URI_TOO_LONG", "414 REQUEST_URI_TOO_LONG", "415 UNSUPPORTED_MEDIA_TYPE", "416 REQUESTED_RANGE_NOT_SATISFIABLE", "417 EXPECTATION_FAILED", "418 I_AM_A_TEAPOT", "419 INSUFFICIENT_SPACE_ON_RESOURCE", "420 METHOD_FAILURE", "421 DESTINATION_LOCKED", "422 UNPROCESSABLE_ENTITY", "423 LOCKED", "424 FAILED_DEPENDENCY", "426 UPGRADE_REQUIRED", "428 PRECONDITION_REQUIRED", "429 TOO_MANY_REQUESTS", "431 REQUEST_HEADER_FIELDS_TOO_LARGE", "451 UNAVAILABLE_FOR_LEGAL_REASONS", "500 INTERNAL_SERVER_ERROR", "501 NOT_IMPLEMENTED", "502 BAD_GATEWAY", "503 SERVICE_UNAVAILABLE", "504 GATEWAY_TIMEOUT", "505 HTTP_VERSION_NOT_SUPPORTED", "506 VARIANT_ALSO_NEGOTIATES", "507 INSUFFICIENT_STORAGE", "508 LOOP_DETECTED", "509 BANDWIDTH_LIMIT_EXCEEDED", "510 NOT_EXTENDED", "511 NETWORK_AUTHENTICATION_REQUIRED"]
				},
				"statusCodeValue": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "ResponseEntity"
		},
		"SearchRequest": {
			"type": "object",
			"properties": {
				"dateFilterType": {
					"type": "string",
					"description": "时间限制",
					"enum": ["ONE_WEEK", "ONE_MONTH", "HALF_YEAR", "ONE_YEAR", "TWO_YEAR"]
				},
				"forumPostType": {
					"type": "string",
					"description": "帖子的类型",
					"enum": ["INQUIRY", "POLL", "EXPERIENCE", "ALL"]
				},
				"keyword": {
					"type": "string",
					"description": "用户搜索词"
				},
				"pageIndex": {
					"type": "integer",
					"format": "int32",
					"example": 0,
					"description": "请求Index"
				},
				"pageSize": {
					"type": "integer",
					"format": "int32",
					"example": 10,
					"description": "请求页数"
				},
				"productIds": {
					"type": "array",
					"description": "相关产品过滤条件",
					"items": {
						"type": "string"
					}
				},
				"searchOrderType": {
					"type": "string",
					"description": "帖子排序",
					"enum": ["DEFAULT", "NEWEST", "READ_MOST"]
				},
				"searchType": {
					"type": "string",
					"description": "检索类型",
					"enum": ["ALL", "KNOWLEDGE", "FORUM"]
				}
			},
			"title": "SearchRequest"
		},
		"SearchResponseInfo": {
			"type": "object",
			"properties": {
				"matchedProducts": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"queryGroupInfo": {
					"$ref": "#/definitions/QueryGroupInfo",
					"originalRef": "QueryGroupInfo"
				}
			},
			"title": "SearchResponseInfo"
		},
		"SearchResultInfo": {
			"type": "object",
			"properties": {
				"estype": {
					"type": "string",
					"enum": ["KNOWLEDGE", "FORUM_POST", "SUGGEST"]
				}
			},
			"title": "SearchResultInfo"
		},
		"SimpleForumPostInfo": {
			"type": "object",
			"properties": {
				"floatSetDate": {
					"type": "string"
				},
				"floatSetUserName": {
					"type": "string"
				},
				"forumId": {
					"type": "integer",
					"format": "int32"
				},
				"message": {
					"type": "string"
				},
				"postId": {
					"type": "integer",
					"format": "int32"
				},
				"threadId": {
					"type": "integer",
					"format": "int32"
				},
				"title": {
					"type": "string"
				}
			},
			"title": "SimpleForumPostInfo"
		},
		"Slot": {
			"type": "object",
			"properties": {
				"name": {
					"type": "string"
				},
				"value": {
					"type": "string"
				}
			},
			"title": "Slot"
		},
		"StatisticsChart": {
			"type": "object",
			"title": "StatisticsChart"
		},
		"SuggestionInfo": {
			"type": "object",
			"properties": {
				"aggCategorySuggestion": {
					"type": "array",
					"example": [],
					"description": "聚合的产品类型的[{id,name}]",
					"items": {
						"$ref": "#/definitions/CategoryInfo",
						"originalRef": "CategoryInfo"
					}
				},
				"inputWordSuggestion": {
					"type": "array",
					"example": [],
					"description": "联想词列表",
					"items": {
						"type": "string"
					}
				}
			},
			"title": "SuggestionInfo"
		},
		"SuggestionRequest": {
			"type": "object",
			"properties": {
				"knowledgeCategoryIds": {
					"type": "array",
					"example": [],
					"description": "用户点击知识类型Id",
					"items": {
						"type": "integer",
						"format": "int32"
					}
				},
				"questionStr": {
					"type": "string",
					"example": "请输入问题前缀",
					"description": "用户输入问题"
				}
			},
			"title": "SuggestionRequest"
		},
		"SystemDocFeedbackPO": {
			"type": "object",
			"properties": {
				"createTime": {
					"type": "string",
					"format": "date-time"
				},
				"feedback": {
					"type": "string"
				},
				"id": {
					"type": "integer",
					"format": "int32"
				},
				"moduleName": {
					"type": "string"
				},
				"userId": {
					"type": "string"
				}
			},
			"title": "SystemDocFeedbackPO"
		},
		"Timestamp": {
			"type": "object",
			"properties": {
				"date": {
					"type": "integer",
					"format": "int32"
				},
				"day": {
					"type": "integer",
					"format": "int32"
				},
				"hours": {
					"type": "integer",
					"format": "int32"
				},
				"minutes": {
					"type": "integer",
					"format": "int32"
				},
				"month": {
					"type": "integer",
					"format": "int32"
				},
				"nanos": {
					"type": "integer",
					"format": "int32"
				},
				"seconds": {
					"type": "integer",
					"format": "int32"
				},
				"time": {
					"type": "integer",
					"format": "int64"
				},
				"timezoneOffset": {
					"type": "integer",
					"format": "int32"
				},
				"year": {
					"type": "integer",
					"format": "int32"
				}
			},
			"title": "Timestamp"
		},
		"URI": {
			"type": "object",
			"properties": {
				"absolute": {
					"type": "boolean"
				},
				"authority": {
					"type": "string"
				},
				"fragment": {
					"type": "string"
				},
				"host": {
					"type": "string"
				},
				"opaque": {
					"type": "boolean"
				},
				"path": {
					"type": "string"
				},
				"port": {
					"type": "integer",
					"format": "int32"
				},
				"query": {
					"type": "string"
				},
				"rawAuthority": {
					"type": "string"
				},
				"rawFragment": {
					"type": "string"
				},
				"rawPath": {
					"type": "string"
				},
				"rawQuery": {
					"type": "string"
				},
				"rawSchemeSpecificPart": {
					"type": "string"
				},
				"rawUserInfo": {
					"type": "string"
				},
				"scheme": {
					"type": "string"
				},
				"schemeSpecificPart": {
					"type": "string"
				},
				"userInfo": {
					"type": "string"
				}
			},
			"title": "URI"
		},
		"URL": {
			"type": "object",
			"properties": {
				"authority": {
					"type": "string"
				},
				"content": {
					"type": "object"
				},
				"defaultPort": {
					"type": "integer",
					"format": "int32"
				},
				"deserializedFields": {
					"$ref": "#/definitions/URLStreamHandler",
					"originalRef": "URLStreamHandler"
				},
				"file": {
					"type": "string"
				},
				"host": {
					"type": "string"
				},
				"path": {
					"type": "string"
				},
				"port": {
					"type": "integer",
					"format": "int32"
				},
				"protocol": {
					"type": "string"
				},
				"query": {
					"type": "string"
				},
				"ref": {
					"type": "string"
				},
				"serializedHashCode": {
					"type": "integer",
					"format": "int32"
				},
				"userInfo": {
					"type": "string"
				}
			},
			"title": "URL"
		},
		"URLStreamHandler": {
			"type": "object",
			"title": "URLStreamHandler"
		},
		"UserInfo": {
			"type": "object",
			"properties": {
				"aggregation": {
					"$ref": "#/definitions/Aggregation",
					"originalRef": "Aggregation"
				},
				"credits": {
					"type": "integer",
					"format": "int32"
				},
				"department": {
					"type": "string"
				},
				"medalidList": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/MedalidInfo",
						"originalRef": "MedalidInfo"
					}
				},
				"relationType": {
					"type": "string",
					"enum": ["NO", "MYSELF", "FOLLOWED", "BE_FOLLOWED", "MUTUAL"]
				},
				"titleAttu": {
					"type": "object"
				},
				"userHeaderPortraitPath": {
					"type": "string"
				},
				"userHonors": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"userId": {
					"type": "string"
				},
				"userName": {
					"type": "string"
				},
				"userTitle": {
					"type": "string"
				},
				"weightedAverage": {
					"type": "number",
					"format": "double"
				}
			},
			"title": "UserInfo"
		},
		"UserSiteInfo": {
			"type": "object",
			"properties": {
				"allowAccessLimitedForum": {
					"type": "integer",
					"format": "int32"
				},
				"boardList": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/ForumBoardInfo",
						"originalRef": "ForumBoardInfo"
					}
				},
				"credit": {
					"type": "integer",
					"format": "int32"
				},
				"department": {
					"type": "string"
				},
				"roleName": {
					"type": "string"
				},
				"userHeaderPortraitPath": {
					"type": "string"
				},
				"userHonors": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"userId": {
					"type": "string"
				},
				"userName": {
					"type": "string"
				},
				"userTitle": {
					"type": "string"
				}
			},
			"title": "UserSiteInfo"
		},
		"View": {
			"type": "object",
			"properties": {
				"contentType": {
					"type": "string"
				}
			},
			"title": "View"
		},
		"ZkUploadResult«string»": {
			"type": "object",
			"properties": {
				"code": {
					"type": "string",
					"example": "0000",
					"description": "response status code",
					"enum": ["0000", "1003", "1001", "1002", "9999", "403"]
				},
				"data": {
					"type": "string",
					"description": "response data body"
				},
				"message": {
					"type": "string",
					"example": "Process succeed",
					"description": "response message body"
				},
				"success": {
					"type": "boolean",
					"example": true,
					"description": "successful or not"
				},
				"uploaded": {
					"type": "integer",
					"format": "int32",
					"example": 1,
					"description": "response uploaded body"
				},
				"url": {
					"type": "string",
					"example": "http://aa/getMedial/aaaa",
					"description": "response uploaded body"
				}
			},
			"title": "ZkUploadResult«string»"
		}
	}
}
'''
data = json.loads(json_text)
paths = data['paths']
for key in paths.keys():
    print(key)
