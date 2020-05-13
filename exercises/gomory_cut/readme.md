# Cấu trúc chương trình
Gồm 4 class:
1. Fraction
- Định nghĩa kiểu dữ liệu phân số
- Gồm một số phương thức tương ứng với các toán tử đơn giản:
	- Plus
	- Minus
	- Multiply
	- Divide
	- Floor
	- Ceil
	- ...
2. Simplex
- Giải bài toán LP (maximize) được cho dưới dạng chính tắc (ràng buộc đẳng thức) và biết trước một cơ sở chấp nhận được
- Input: ./data/simplex_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- Dòng thứ i trong m dòng tiếp theo:
		- n số đầu tiên là các số hữu tỉ, số thứ j là hệ số của các biến x_j trong ràng buộc thứ i.
		- Số thứ n+1 là một số hữu tỉ, là giá trị vế phải của ràng buộc.
		- Số thứ n+2 là một số nguyên, chỉ số của biến cơ sở tương ứng với ràng buộc (chỉ số bắt đầu từ 0).
	- Dòng cuối cùng gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
3. TwoPhaseSimplex
- Giải bài toán LP (maximize) được cho dưới dạng chính tắc (ràng buộc đẳng thức) và chưa biết bất kỳ cơ sở chấp nhận được nào
- Input: ./data/twophase_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- Dòng thứ i trong m dòng tiếp theo:
		- n số đầu tiên là các số hữu tỉ, số thứ j là hệ số của các biến x_j trong ràng buộc thứ i.
		- Số thứ n+1 là một số hữu tỉ, là giá trị vế phải của ràng buộc.
	- Dòng cuối cùng gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
4. GomoryTwoPhaseSimplex
- Giải bài toán MILP (maximize) được cho dưới dạng chính tắc (ràng buộc bất đẳng thức), trong đó có một số biến bị ràng buộc nguyên
- Input: ./data/gomory_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- Dòng thứ i trong m dòng tiếp theo:
		- n số đầu tiên là các số hữu tỉ, số thứ j là hệ số của các biến x_j trong ràng buộc thứ i.
		- Số thứ n+1 là một số hữu tỉ, là giá trị vế phải của ràng buộc.
	- Dòng thứ m + 2 gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
	- Dòng thứ m + 3 gồm một số n' là số lượng biến bị ràng buộc nguyên
	- Dòng cuối cùng có n' số nguyên, là chỉ số của các biến bị ràng buộc nguyên

# Cách chạy chương trình
1. Môi trường
- Chương trình được viết trên hệ điều hành Windows, được compile bằng java compiler 1.8 và chạy thành công bằng JRE 1.8.
2. Thay đổi input
- Mỗi class đều có một hàm main() được dùng để test chức năng của class đó.
- Với các class GomoryTwoPhaseSimplex, TwoPhaseSimplex và Simplex thì đầu mỗi hàm main() đều có một biến fis chứa thông tin đường dẫn đến file input, ta chỉ cần tạo một file input hợp lệ và thay đổi đường dẫn đến file input này.
3. Compile
- Chạy lệnh `javac A.java` để biên dịch class A.
4. Chạy chương trình
- Sau khi compile thành công, chạy lệnh `java A` để chạy class A.