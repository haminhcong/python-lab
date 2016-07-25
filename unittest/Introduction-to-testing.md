#Testing trong Flask
Một trong các công đoạn quan trọng trong quá trình xây dựng một phần mềm, đó là công đoạn kiểm thử phần mềm. Kiểm thử phần mềm là kiểm tra chất lượng của phần mềm đó, với nhiều phương pháp kiểm tra khác nhau, nhằm:

- Đảm bảo phần mềm hoạt động đúng như yêu cầu đặt ra.
- Chứng minh chất lượng của phần mềm với các bên liên quan (được chứng minh bằng các kết quả kiểm tra, các tài liệu, biên bản...)
- Phát hiện ra các lỗi (nếu có)

Để hỗ trợ cho việc kiểm thử phần mềm, python có cài đặt sẵn package unittest. Trong bài viết này, chúng ta sẽ tìm hiểu cách sử dụng unittest để kiểm tra một số phương thức trong một chương trình đã được xây dựng.

##Sử dụng unittest package để kiểm thử mã nguồn python
###Mô hình kiểm thử

Khi sử dụng unittest package để kiểm thử mã nguồn, chúng ta sẽ xây dựng một chương trình kiểm thử dựa trên 1 lớp dẫn xuất của lớp ```unittest.TestCase```, lớp này sẽ bao gồm các thành phần sau:
- Phương thức ```setUp(self)```: Chúng ta sẽ thiết lập môi trường kiểm thử trong thân phương thức này( ví dụ như thêm các biến global, thiết lập các cấu hình của phần mềm sẽ kiểm thử, kết nối cơ sở dữ liệu...)

- Các phương thức ```test_xxx```: Các phương thức cần kiểm tra sẽ đặt trong các phương thức có tên bắt đầu bằng ```test```. Mô hình chung là các phương thức này sẽ thiết lập tập giá trị đầu vào, sau đó chạy phương thức cần kiểm tra, rồi thiết lập các lệnh kiểm tra giá trị đầu ra, ở đây chúng ta sử dụng các lệnh ```assert``` để kiểm tra giá trị đầu ra của phương thức cần kiểm tra.

- Phương thức ```tearDown(self)```: Chúng ta sử dụng phương thức này để kết thúc chương trình kiểm tra (Hủy kết nối, đóng file hoặc xóa các file tạm, ....

Sau đây, chúng ta sẽ dùng 1 ví dụ để  minh họa cách sử dụng unittest package để kiểm thử
###Ví dụ
Chúng ta sẽ kiểm thử một hàm đơn giản bằng unittest package. Ta sẽ xây dựng lớp mô tả một tài khoản ngân hàng
```python
class BankAccount:
    def __init__(self,init_balance):
        if init_balance <= 1000:
            raise ValueError('initial balance must be > 1000 ')
        self.balance = init_balance

    def deposit(self,amount):
        if amount <= 1:
            return "error"
        else:
            self.balance+=amount
            return "Success"

    def withdraw(self,amount):
        self.balance-=amount
        return "Success"

    def check_balance(self):
        return self.balance

```
Chúng ta sẽ kiểm tra lớp trên bằng các test case sau:

- Test case 1: Tạo 1 tài khoản với số tiền ban đầu 5000, sau đó rút 3000. Kết quả trả về sẽ là ```Success``` nếu đúng
- Test case 2: Tạo 1 tài khoản với số tiền ban đầu -5000. Kết quả đúng nếu có exception xảy ra.
- Test case 3: Tạo 1 tài khoản với số tiền ban đầu 5000, sau đó nạp -3000. Kết quả trả về sẽ là ```erorr``` nếu đúng
- Test case 4: Tạo 1 tài khoản với số tiền ban đầu 5000, sau đó rút 8000. Kết quả trả về sẽ là ```error``` nếu đúng

(Đây chỉ là một số test case sử dụng làm ví dụ minh họa. Trong trường hợp thực tế, số lượng test case sẽ lớn hơn rất nhiều 4 test case trên
Thiết kế các test:
```python
    def test_case_1(self):
        a = BankAccount(5000)
        result = a.withdraw(3000)
        assert 'success' in result

    def test_case_2(self):
        with self.assertRaises(ValueError) as context:
            a = BankAccount(-5000)
        self.assertTrue('initial balance must be > 1000' in context.exception)

    def test_case_3(self):
        a = BankAccount(5000)
        result = a.deposit(-3000)
        assert 'error' in result

    def test_case_4(self):
        a = BankAccount(5000)
        result = a.withdraw(8000)
        assert 'error' in result
```
Kết quả chạy test:
![test-result.png](test-result.png)



