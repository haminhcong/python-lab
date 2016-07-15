#Python fundamental
##1 Object
###1.1 Python Scopes
Trong Python, chúng ta có thể bắt gặp trường hợp, có nhiều đối tượng khác nhau được các tên riêng (name) trùng tên ánh xạ tới. Ví dụ
```python
a=10
def fn():
    a=8
fn()
print(a)
```
trong trường hợp này, a ở câu lệnh cuối cùng ```print(a)``` sẽ nhận giá trị là bao nhiêu?
do đó ta cần giải quyết vấn đề sau: một trên riêng đang được ánh xạ tới đối tượng nào trong chương trình tại thời điểm thực thi?
Vấn đề trên được python giải quyết bằng LEGB rule, đây là một quy tắc tìm kiếm ánh xạ của một tên riêng tới đối tượng. Theo quy tắc này tại một thời điểm bất kỳ tồn tại 4 phạm vi (scope) sau:

![scope-python.png](./img/scope-python.png)
Trong đó:

- Local: Là phạm vi của hàm, phương thức,... đang bao trong nhất câu lệnh chứa tên riêng đang xét

- Enclosed: Là phạm vi của các hàm, các phương thức,... bao quanh phạm vi Local

- Global: Là phạm vi ngoài nhất, bao trùm toàn bộ chương trình đang thực thi.

- Built-in: Là phạm vi của các hàm, các phương thức, các thư viện được Python xây dựng sẵn.

Ví dụ, với nội dung 1 file test.py như sau:
```python
#tes.py content
a_var = 'global value'
b_var = 'another'
c_var = a_var+b_var
def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()
```

Ta xét ánh xạ của tên riêng ```a_var``` trong câu lệnh ```print(a_var)```. Lúc này, đối với tên riêng ```avar``` thì:

- phạm vi trong hàm inner() là Local scope

- Phạm vi trong hàm outer() là Enclosed scope

- Các câu lệnh

```python
a_var = 'global value'
b_var = 'another'
c_var = a_var+b_var
def outer()
outer()
```
thuộc Global scope

Khi xác định xem một tên riêng đang ánh xạ tới đối tượng nào trong chương trình, trình biên dịch của Python bắt đầu tìm kiếm ánh xạ tới tên riêng từ phạm vi Local. Nếu không tìm thấy, nó chuyển tiếp lên tìm kiếm ở phạm vi Enclosed, rồi Global, rồi Built-in. Nếu không tìm thấy, một exception xảy ra.

Ta xét tiếp 1 ví dụ khác, xem trong trường hợp sau kết quả in ra là gì:
```python
a = 'global'

def outer():

    def len(in_var):
        print('called my len() function: ')
        l = 0
        for i in in_var:
            l += 1
        return l

    a = 'local'

    def inner():
	a='inner'
        a += ' variable'
    inner()
    print('a is', a)
    print(len(a))


outer()

print(len(a))
print('a is', a)
```
Ta thấy, khi câu lệnh outer ở Global scope được thực thi, thì hàm outer() được thực thi. Trong hàm outer, a được gán object là 'local'. Khi câu lệnh inner() được gọi, tên riêng a lại được gán cho object 'inner'. Lúc này, ta cần hiểu rằng tuy 2 tên riêng này trùng tên nhưng lại ánh xạ tới 2 đối tượng khác nhau và là 2 tên riêng khác nhau. Bởi vì, khi câu lệnh a='inner' được thực thi sẽ tạo ra 1 tên riêng ```a``` mới ánh xạ tới object 'inner'. Do đó 2 tên riêng ```a``` ở inner và outer là 2 tên riêng hoàn toàn khác nhau.

Do đó sau khi thực hiện xong hàm inner(), giá trị của a trong hàm outer không đổi, do đó câu lệnh ``` print('a is', a)``` sẽ là ```a is local```. Bởi vì, đối với câu lệnh này, local của nó là thân hàm outer(). Khi tìm kiếm trên thâm hàm outer, nó tìm thâý ánh xạ  a = 'local', nên nó không cần tìm ra bên ngoài nữa. Và tương tự với trường hợp trên, a ='global' và a='local' là 2 tên riêng hoàn toàn khác nhau. Do đó trong trường hợp này, ta sẽ có 3 tên riêng a khác nhau nhưng trùng tên ánh xạ tới 3 đối tượng.
###1.2 Python Object
###1.2.1 Khai báo lớp trong Python
- Python sử dụng câu lệnh ```Class <class name>:``` để khai báo một lớp. Ví dụ
```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
Đoạn lệnh trên định nghĩa 1 class mới là MyClass.

- Để tạo ra 1 thực thể có tên là x của lớp MyClass:
```python
	x= MyClass()
```
- Để viết phương thức khởi tạo cho class MyClass, chúng ta cần thêm vào định nghĩa của MyClass phương thức ```def __init__():```. Ví dụ
```python
class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self, x1, x2):
        self.a = x1
        self.b = x2
    def f():
        return 'hello world'
    def fk(self):
        return (self.a+self.b)

```
- Phân biệt thuộc tính của lớp và thuộc tính của thực thể:

Ở trong một lớp trong python có thể tồn tại 2 loại thuộc tính: thuộc tính của lớp và thuộc tính của thực thể. Thuộc tính của lớp là thuộc tính chung cho mọi đối tượng thuộc lớp đó và cho cả lớp đó, tương tự như thuộc tính có định danh ```static``` của các ngôn ngữ lập trình khác. Thuộc tính thực thể là các thuộc tính của riêng các thực thể trong lớp đó, các thuộc tính này được khai báo ngay trong phương thức khởi tạo. Ví dụ, trong khai báo của lớp MyClass như trên, thì a và b là 2 thuộc tính thực thể. Ta có thể lấy thêm 1 ví dụ về 2 loại thuộc tính này:
```python
y1 = MyClass(3,4)
y2 = MyClass(5,6)
```
Lúc này ta sẽ có y1.a=3, còn y1.b =5. Không có thuộc tính MyClass.a. Tuy nhiên, ta sẽ có y1.i=y2.i=MyClass.i=12345. Đó chính là sự khác biệt giữa thuộc tính lớp và thuộc tính thực thể.

Tương tự như thuộc tính, các phương thức được khai báo bên trong lớp có thể được sử dụng bằng cả tên lớp và cả từ các thực thể trong lớp đó. Tuy nhiên, trong trường hợp phương thức đó có tác động đến các thực thể của lớp, khi sử dụng phương thức với tên lớp sẽ có thể gây lỗi. Ví dụ, ta có thể sử dụng MyClass.f() mà không có lỗi gì. Tuy nhiên, khi sử dụng MyClass.fk() sẽ gây ra 1 exception, do MyClass không chứa self, nên self.a và self.b không tồn tại.

- Từ khóa ```self``` đại diện cho thực thể của lớp đó, tương tự từ khóa this trong C#, Java.
###1.2.2 Kế thừa và đa hình trong Python
- Python cho phép một lớp có thể kế thừa từ 1 lớp hay nhiều lớp khác. Ví dụ

```python
class A():
    x1 = 10
    x2 = 8

    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    def show(self):
        return self.a + self.b

    def rep(self):
        return self.a*self.b

class B(A):
    def __init__(self,a1,b1,c1,d1):
        super().__init__(a1,b1)
        self.c=c1
        self.d=d1
    def show(self):
        x=super().show()
        return x+self.c+self.d

a1 =A(5,6)
b1 =B(1,2,3,4)
print(b1.show())
print(a1.show())
print(b1.rep())

10
11
2
```
- Để gọi tới phương thức của lớp cha bị override, ta sử dụng từ khóa super(), ví dụ  ``` super().show()``` hoặc ```super(A,self).show()```

##2 Iterator & Generator
2 khái niệm này trong python dùng để tạo ra các đối tượng Iterable object, tức là các đối tượng có thể duyệt qua được. Đầu tiên chúng ta cần hiểu về Iterable object.
##2.1 Iterable object
Iterable object là khái niệm dùng để chỉ các đối tượng có chứa một tập hợp các phần tử cùng kiểu, và đối tượng này có thể dùng từ khóa for để duyệt qua. Ví dụ:
```python
x = [1,2,3,4]
for i in x:
    print(i*2)
y = ("a","b","c","d")
for i in y:
    print(i)
z = {"a":"International", "b":1, "c": "look"}
for key,value in z.items():
    print (key+":"+str(value))
```
Có thể thấy, ở ví dụ trên ta có 3 iterable object là x, y, z, trong đó x là list object, y là tuple, z là dictionary. 3 đối tượng này đều có đặc điểm chung là chứa 1 tập hợp các phần tử cùng kiểu, và đều dùng cấu trúc for i in object để duyệt qua tập hợp phần tử trên.

Vậy, làm thế nào để xác định 1 đối tượng là một iterable objet?
##2.2 Iterator
=> Một iterable object được định nghĩa là một đối tượng chứa phương thức ```__iter__()```, và kết quả trả về của phương thức này là ```iterator object```.

=> Một ```iterator``` object là một đối tượng có chứa phương thức ```next()```. Phương thức ```next()``` trả về kết quả là một phần tử. Nếu không còn phần tử nào nữa, phương thức ```next()``` gây ra exception ```StopIteration```. Ví dụ
```python
x = [1,2,3,4]
y = x.__iter__()
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())

1
2
3
4
Traceback (most recent call last):
  File "/home/cong/PycharmProjects/python-lab/flask-begin-to-dream/run_batch.py", line 7, in <module>
    print(y.__next__())
StopIteration
```
Chúng ta có thể thấy là x chỉ có 4 phần tử, do đó khi gọi tới phương thức print thứ 5 thì ```StopIteration``` Exception được thả.

Điều tiếp theo chúng ta quan tâm là làm thế nào để tạo ra các lớp có khả năng tạo ra các iterable object ?. Chúng ta có thể áp dụng định nghĩa, tạo ra các iterator object bằng cách thêm vào class các phương thức ```__iter__()``` và ```__next__()```. Ví dụ
```python
class A:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.i=min
    def __iter__(self):
        return self
    def __next__(self):
        if(self.i<=self.max):
            self.i+=1
            return (self.i-1)
        else:
            self.i=self.min
            raise StopIteration

x= A(4,8)
for i in x:
    print(i)

#Ket qua
4
5
6
7
8

Process finished with exit code 0
```
##2.3 Generator
Như vậy, với việc tạo ra các object có các phương thức ```__iter__()``` và ```__next__()```, chúng ta có thể tạo ra các đối tượng ```iterator```. Tuy nhiên, chúng ta có thể tạo ra các đối tượng iterator một cách đơn giản hơn bằng cách sử dụng ```generator```.

```Generator``` là một function tạo ra iterator. function này tạo ra iterator bằng từ khóa yield. Khác với các function thông thường, function này không sử dụng return để trả về, mà mỗi một câu lệnh yield sẽ tạo ra một phần tử trong iterator được tạo ra.

Ví dụ:
```python
def generatorA(min,max):
    while min<=max:
        yield min
        min+=1

for x in generatorA(4,8):
    print(x)

4
5
6
7
8

Process finished with exit code 0

```
chúng ta có thể thấy việc sử dụng generator tiện lợi hơn nhiều so với việc phải định nghĩa các phương thức ```__iter__()``` và ```__next()__```
##3 Future
Chúng ta có thể thấy, các phiên bản của python có những sự khác nhau. Đồng thời, phiên bản mới của Python có thể có những tính năng, từ khóa mới mà phiên bản cũ chưa có. Vì vậy, kể từ phiên bản 2.1, python sử dụng từ khóa ```__future__`` cho phép người dùng ở các phiên bản cũ sử dụng các tính năng của các phiên bản mới.
Ví dụ, ở phiên bản 2.7, với việc không sử dụng từ khóa future
```python
cong@cong-HP-ProBook-450-G1:~$ python2
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print 8/7
1
>>> print 8//7
1
```
Kết quả của 2 phép chia đều là 1.Bây giờ nếu sử dụng package division bằng ```__future__```:
```python
cong@cong-HP-ProBook-450-G1:~$ python2
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import division
>>> print 8/7
1.14285714286
>>> print 8//7
1
>>> 
```
Ta sẽ có thể sử dụng phép chia 8/7 để chia theo kiểu thương là số thực. Còn phép chia 8//7 sẽ cho kết quả chia lấy phần nguyên. Đây là các tính năng mà python3 hỗ trợ, và có thể sử dụng ở python2 thông qua ```__future__```

Một ví dụ khác, ở python2 print được sử dụng như sau
```python
cong@cong-HP-ProBook-450-G1:~$ python2
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a="hello"
>>> print a
hello

```
Nếu dùng future import package print_statement thì ta sẽ phải sử dụng print theo kiểu của python3, tức là sử dụng như 1 hàm:
```python
cong@cong-HP-ProBook-450-G1:~$ python2
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a="hello"
>>> print a
hello
>>> from  __future__ import print_function
>>> print a
  File "<stdin>", line 1
    print a
          ^
SyntaxError: invalid syntax
>>> print(a)
hello

```
