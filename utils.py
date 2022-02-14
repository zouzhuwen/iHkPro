#公共断言方法

def common_assert(case,response,status_code=200,success=True,returnCode="0000",returnMsg="Success"):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(success, response.json().get("success"))
    case.assertEqual(returnCode, response.json().get("returnCode"))
    case.assertIn(returnMsg, response.json().get("returnMsg"))
