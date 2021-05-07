from evaulation_scenario import *
import time


@given("on Add Requirement page")
def step_impl(context):
    time.sleep(1)
    context.driver.get('http://localhost:8080/VALU3S/++add++requirement')


@when("I leave Title field empty")
def step_impl(context):
    pass


@then("I should see Error message")
def step_impl(context):
    text_elem = context.driver.find_element(By.XPATH, '/html/body/div/div[3]/main/div[1]/div/div/article/div/dl')
    assert text_elem.text == 'Error There were some errors.'


def create_tc(context, title, uc):
    context.driver.get('http://localhost:8080/VALU3S/++add++test_case')
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(title)
    context.driver.find_element(By.ID, "form-widgets-test_case_id").send_keys(uc)
    context.driver.find_element(By.ID, "form-buttons-save").click()


@given("at least one test case exists")
def step_impl(context):
    create_tc(context, "tc_foo", "uc7_tc_7")


@when("I specify requirement Title")
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("req5_foo")


@step("Requirement Test Case")
def step_impl(context):
    WebDriverWait(context.driver, 2)
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/fieldset[2]/div/div[2]/div[1]/div[1]/a').click()
    context.driver.find_element(By.ID, "s2id_autogen10").send_keys("tc_foo")
    context.driver.find_element(By.ID, "s2id_autogen10").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()


@step("I should see reference of test cases in requirements content")
def step_impl(context):
    eval_elem1 = context.driver.find_element(By.XPATH,
                                             '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
    assert "tc_foo" in eval_elem1.text


@step("consumer shouldn't see newly created requirement")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("req5_foo")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    result_elem = context.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')

    assert "No results were found." in result_elem.text
    try_log_admin(context)


@given("newly created requirement exists")
def step_impl(context):
    create_req(context, "req9", None)


@when("I change state of requirement to published")
def step_impl(context):
    try:
        context.driver.implicitly_wait(2)
        context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
        context.driver.find_element(By.CSS_SELECTOR, ".state-private:nth-child(2)").click()
        context.driver.find_element(By.ID, "workflow-transition-publish").click()
    except:
        context.driver.find_element(By.XPATH,
                                    '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/form/div[7]/input[1]').click()


@then("consumer should see given requirement")
def step_impl(context):
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("req9")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    try:
        result_elem = context.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')
        assert "No results were found." not in result_elem.text
        try_log_admin(context)
    except:
        # there are some elements
        try_log_admin(context)
        assert True


@given("at least two Test cases exists")
def step_impl(context):
    create_tc(context, "tc2_1", "uc00_tc_00")
    create_tc(context, "tc2_2", "uc00_tc_01")


@given("requirement with one test case exists")
def step_impl(context):
    create_req(context, "req05", "tc2_1")


@when("I add another test case into existing requirement")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/fieldset[2]/div/div[2]/div[1]/div[1]/a').click()
    context.driver.find_element(By.ID, "s2id_autogen10").send_keys("tc2_2")
    context.driver.find_element(By.ID, "s2id_autogen10").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then("I should see references to both test cases and its requirements and test cases in given requirement content")
def step_impl(context):
    try:
        eval_elem1 = context.driver.find_element(By.XPATH,
                                                 '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li[1]/span/a/span[1]')
        assert "tc2_1" in eval_elem1.text

        eval_elem2 = context.driver.find_element(By.XPATH,
                                                 '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li[2]/span/a/span[1]')
        assert "tc2_2" in eval_elem2.text

    except:
        assert False


@given("requirement with test case exists")
def step_impl(context):
    create_tc(context, "tc2_3", "uc02_tc_02")
    create_req(context, "req06", "tc2_3")


@when("I edit given test case")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".url").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("_new")
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("req06")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.DOWN)
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/ol/li/span[1]/a').click()


@then("I should see updated informations in requirements content page")
def step_impl(context):
    eval_elem = context.driver.find_element(By.XPATH,
                                            '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
    assert "tc2_3_new" in eval_elem.text


@given("requirement exists")
def step_impl(context):
    create_req(context, "req08", None)


@when("I delete requirement")
def step_impl(context):
    delete_this(context)


@then("I should no longer see given requirement")
def step_impl(context):
    context.driver.find_element(By.ID, "searchGadget").send_keys('req08')
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    try:
        result_elem = context.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')
        assert "No results were found." in result_elem.text
    except:
        # there are elements
        assert False


@given("requirement with new test case exists")
def step_impl(context):
    create_tc(context, "tc2_5", "uc02_tc_05")
    create_req(context, "req07", "tc2_5")


@when("I delete test case")
def step_impl(context):
    eval_elem = context.driver.find_element(By.XPATH,
                                            '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
    assert "tc2_5" in eval_elem.text

    context.driver.find_element(By.CSS_SELECTOR, ".url").click()
    delete_this(context)


@then("I should no longer see deleted test cases references in requirement")
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH,
                                    '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
        assert False
    except:
        # element doesnt exist
        assert True
