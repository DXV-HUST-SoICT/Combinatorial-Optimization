# Thuật toán 1: Tabu search
- Khởi tạo lời giải:
	- Số lượng màu được dùng bằng số đỉnh của đồ thị.
	- Gán ngẫu nhiên cho mỗi đỉnh một màu (theo phân phối chuẩn).
- Search:
	- Thử giảm dần lượng màu có thể dùng để tô màu
	- Với mỗi số màu cố định, thực hiện thử cho đến khi tìm được lời giải `feasible` hoặc đạt số lần thử tối đa:
		- Thực hiện tabu search:
			- Lựa chọn 1 node có violation > 0, không nằm trong tabu list và có violation lớn nhất. Nếu có nhiều node có cùng violation lớn nhất, ta chọn ngẫu nhiên 1 node.
			- Nếu không tìm được node phù hợp, ta xoá 1 node khỏi tabu list và tìm lại.
			- Thêm node tìm được vào tabu list.
			- Đổi màu node vừa tìm được, màu mới phải thoả mãn:
				- Khác màu ban đầu
				- Ít conflict với hàng xóm nhất
				- Nếu có nhiều màu thoả mãn, ta chọn ngẫu nhiên theo phân phối chuẩn
		- Thực hiện xoá ngẫu nhiên 1 màu `x` (restart):
			- Tất cả các đỉnh có màu `x` được tô lại bằng 1 màu ngẫu nhiên khác `x` theo phân phối chuẩn

# Thuật toán 2: Iterated Greedy
- Lặp lại các bước:
	- Tô màu tham lam
	- Sinh hoán vị mới:
		- Khởi tạo list rỗng
		- Lặp:
			- Chọn ngẫu nhiên 1 nhóm các đỉnh cùng màu, sắp xếp theo thứ tự giảm dần của bậc rồi append vào list cho đến khi không còn màu nào