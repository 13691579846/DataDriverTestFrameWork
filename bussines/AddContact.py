from pages.HomePage import HomePage
from pages.NewContactPage import AddContactPage


class NewContactPersonAction(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.new_contact_page = AddContactPage(self.driver)

    def address_link(self):
        """点击通讯录按钮"""
        self.home_page.address_link.click()

    def add_contact(self, contact_name, contact_mail, is_star, contact_phone, contact_comment):
        """添加联系人场景"""
        # 点击新建联系人
        self.new_contact_page.new_contact.click()
        if contact_name:
            # 非必填项
            self.new_contact_page.add_name.send_keys(contact_name)
        # 必填项
        self.new_contact_page.add_mail.send_keys(contact_mail)
        if is_star == '是':
            self.new_contact_page.mark_star.click()
        if contact_phone:
            self.new_contact_page.add_phone.send_keys(contact_phone)
        if contact_comment:
            self.new_contact_page.add_content.send_keys(contact_comment)
        self.new_contact_page.click_commit_btn.click()


if __name__ == '__main__':
    pass
