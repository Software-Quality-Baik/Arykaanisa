import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Membuka halaman login
        self.driver.get("https://healhero.my.id/signin.html")

        # Mencari elemen input username dan password menggunakan XPath
        email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def cek_home(self):
        # Membuka halaman cek kesehatan
        self.driver.get("https://healhero.my.id/pengguna/index.html")

        time.sleep(2)

        # Lakukan pengujian cek kesehatan
        # Lakukan implementasi pengujian cek kesehatan di sini
    def cek_kesehatan(self):
        # Membuka halaman cek kesehatan
        self.driver.get("https://healhero.my.id/pengguna/cekkesehatan.html")

        time.sleep(2)

        # Lakukan pengujian cek kesehatan
        # Lakukan implementasi pengujian cek kesehatan di sini

    def cek_polatidur(self):
        # Membuka halaman cek pola tidur
        self.driver.get("https://healhero.my.id/pengguna/cekpolatidur.html")

        time.sleep(2)

        # Mencari elemen input menggunakan ID
        sleepTime_input = self.driver.find_element(By.ID, "sleepTime")
        wakeTime_input = self.driver.find_element(By.ID, "wakeTime")
        # carbs_input = self.driver.find_element(By.ID, "carbs")
        # fat_input = self.driver.find_element(By.ID, "fat")

        # Memasukkan nilai ke dalam input
        sleepTime_input.send_keys("09.00")
        wakeTime_input.send_keys("10.00")
        # carbs_input.send_keys(carbs)
        # fat_input.send_keys(fat)

        # Tunggu hingga tombol submit muncul
        time.sleep(2)

        # Klik tombol Submit
        button = self.driver.find_element(By.XPATH, '//button[@type="button"]')
        button.click()

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("putri1@gmail.com", "putricantik")
        
        self.cek_home()

        # Jalankan pengujian cek kesehatan
        self.cek_kesehatan()

        # Jalankan pengujian cek pola tidur
        self.cek_polatidur()


if __name__ == "__main__":
    unittest.main()

