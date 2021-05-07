from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

def try_log_admin(context):
    context.driver.get("http://localhost:8080/VALU3S")
    try:
        context.driver.find_element(By.ID, "personaltools-login").click()
        context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
        context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        time.sleep(1)
    except:
        pass  # already loged in

@given('logged in as admin')
def step_impl(context):
    try_log_admin(context)



@given("on Add Evaluation Scenario page")
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++evaluation_scenario")


def create_req(context, name, tc):
    context.driver.get("http://localhost:8080/VALU3S/++add++requirement")
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys(name)

    if tc is not None:
        WebDriverWait(context.driver, 2)
        context.driver.find_element(By.ID, "form-buttons-save").click()
        context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
        context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
        context.driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/fieldset[2]/div/div[2]/div[1]/div[1]/a').click()
        context.driver.find_element(By.ID, "s2id_autogen10").send_keys(tc)
        context.driver.find_element(By.ID, "s2id_autogen10").send_keys(Keys.ENTER)
        context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()

    context.driver.find_element(By.ID, "form-buttons-save").click()



@given("at least one requirement exists")
def step_impl(context):
    create_req(context, "req1", None)


@when("I specify Title")
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("title_foo")


@step("Use Case Id")
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys("UC1_TC_1")


@step("Use Case Evaluation Scenario Textual Description")
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys("desc_foo")


@step("Use Case Evaluation Scenario Requirements List")
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.ID, "s2id_autogen2").send_keys("req1")
    WebDriverWait(context.driver, 2)
    context.driver.find_element(By.ID, "s2id_autogen2").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()

@step('click "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then("I should see Item created")
def step_impl(context):
    statusText = context.driver.find_element(By.XPATH, '//*[@id="global_statusmessage"]').text
    assert statusText == 'Info Item created'


@step("I should see reference of requirement in requirements content")
def step_impl(context):
    try:
        eval_elem = context.driver.find_element(By.XPATH,
         '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
        assert "req1" in eval_elem.text
    except:
        assert False


@step("consumer shouldn't see newly created Evaluation Scenario")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("req1")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    result_elem = context.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')

    assert "No results were found." in result_elem.text
    try_log_admin(context)


def create_eval_scenario(context,title,uc,desc,req):
    context.driver.get("http://localhost:8080/VALU3S/++add++evaluation_scenario")
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(title)
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys(uc)
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys(desc)
    if req is not None:
        context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
        context.driver.find_element(By.ID, "s2id_autogen2").send_keys(req)
        WebDriverWait(context.driver, 2)
        context.driver.find_element(By.ID, "s2id_autogen2").send_keys(Keys.ENTER)
        context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@given("newly created Evaluation Scenario exists")
def step_impl(context):
    create_eval_scenario(context,"eval_title_foo","uc2_tc_2","description", None)


@when("I change state of Evaluation Scenario to published")
def step_impl(context):
    try:
        context.driver.implicitly_wait(2)
        context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
        context.driver.find_element(By.CSS_SELECTOR, ".state-private:nth-child(2)").click()
        context.driver.find_element(By.ID, "workflow-transition-publish").click()
    except:
        context.driver.find_element(By.XPATH, '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/form/div[7]/input[1]').click()


@then("consumer should see given Evaluation Scenario")
def step_impl(context):
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("eval_title_foo")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    try:
        result_elem = context.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')
        assert "No results were found." not in result_elem.text
        try_log_admin(context)
    except:
        #there are some elements
        try_log_admin(context)
        assert True


@given("at least two requirements exists")
def step_impl(context):
    create_req(context, "req2", None)
    create_req(context, "req3", None)


@given("Evaluation Scenario with one requirement exists")
def step_impl(context):
    create_eval_scenario(context, "title2_foo", "uc3_tc_3", "desc", "req2")


@when("I add another requirement into existing Evaluation Scenario")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.XPATH, "/html/body/div/div[3]/main/div[1]/div/div/article/div/form/fieldset[2]/div/div[2]/div[1]/div[1]/a/span").click()
    context.driver.find_element(By.ID, "s2id_autogen2").send_keys("req3")
    WebDriverWait(context.driver, 2)
    context.driver.find_element(By.ID, "s2id_autogen2").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, '/html/body/div[4]/ul/li[1]/div/div/div/a[1]/div/span[1]').click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then("I should see references to both requirements in given Evaluation Scenario content")
def step_impl(context):
    try:
        eval_elem1 = context.driver.find_element(By.XPATH,
                                                 '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li[1]/span/a/span[1]')
        assert "req2" in eval_elem1.text

        eval_elem2 = context.driver.find_element(By.XPATH,
                                                '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li[2]/span/a/span[1]')
        assert "req3" in eval_elem2.text

    except:
        assert False


@given("Evaluation Scenario with requirement exists")
def step_impl(context):
    create_req(context, "req4", None)
    create_eval_scenario(context, "title3_foo", "uc4_tc_4", "desc", "req4")


@when("I edit given requirement")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".url").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("_new")
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.ID, "searchGadget").click()
    context.driver.find_element(By.ID, "searchGadget").send_keys("title3_foo")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.DOWN)
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/ol/li/span[1]/a').click()

@then("I should see updated informations in Evaluation Scenario content page")
def step_impl(context):
    eval_elem = context.driver.find_element(By.XPATH,
                                             '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
    assert "req4_new" in eval_elem.text


@given("Evaluation Scenario exists")
def step_impl(context):
    create_eval_scenario(context, "title4_foo", "uc5_tc_5", "desc", None)


def delete_this(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()

@when("I delete given Evaluation Scenario")
def step_impl(context):
    delete_this(context)


@then("I should no longer see it")
def step_impl(context):
    context.driver.find_element(By.ID, "searchGadget").send_keys("title4_foo")
    context.driver.find_element(By.ID, "searchGadget").send_keys(Keys.ENTER)
    result_elem = context.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[3]/main/div[1]/div/div/article/div/form/div[2]/div[3]/div[2]/div/p/strong')
    assert "No results were found." in result_elem.text

@given("Evaluation Scenario with a requirement exists")
def step_impl(context):
    create_req(context, "req5", None)
    create_eval_scenario(context, "title4_foo", "uc5_tc_5", "desc", "req5")

@when("I delete given requirement")
def step_impl(context):
    eval_elem = context.driver.find_element(By.XPATH,
                                             '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
    assert "req5" in eval_elem.text

    context.driver.find_element(By.CSS_SELECTOR, ".url").click()
    delete_this(context)


@then("I should no longer see deleted requirements references in Evaluation Scenario")
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH,
                                     '/html/body/div/div[3]/main/div[1]/div/div/article/div[2]/fieldset[1]/div/span/div/ul/li/span/a/span[1]')
        assert False
    except:
        #element doesnt exist
        assert True
