# NLP_VQA

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Cấu trúc repo
- Thư mục `data` chứa toàn bộ dữ liệu dùng để finetune (phần dữ liệu TextVQA và VQAv2 do quá nặng nên link được để trong phần lời mở đầu của bài báo cáo)
- Thư mục `eval_result` chứa kết quả đánh giá mô hình
- Thư mục `model `chứa phần code được sử dụng để làm các bước thí nghiệm về việc fine-tune, sau đấy bộ tham số tốt nhất sẽ được đóng gói và cập nhật trong thư mục `fine_tune`. Để chạy thư mục này, bạn chỉ cần đẩy các file .ipynb lên google colab hoặc kaggle rồi chạy từng cells.
- Thư mục `fine_tune` chứa các tham số và code phần finetune có kết quả tốt nhất sau khi chạy các thí nghiệm.

## Website demo (Hugging Face)
- [Link](https://huggingface.co/spaces/triphuong57/paligemma_ft_v1)


## Thành viên nhóm
- Nguyễn Quý Đang - 22022500 
- Đỗ Minh Nhật - 22022537
- Vũ Vân Long - 22022501

## Phân công công việc
| Họ và Tên | Công việc |
|-----------|-----------|
| Nguyễn Quý Đang | - Phân công công việc cho thành viên nhóm<br>- Tìm hiểu tổng quan về mô hình PaliGemma<br>- Finetune mô hình PaliGemma<br>- Dựng demo mô hình PaliGemma<br>- Làm slide<br>- Xem xét, chỉnh sửa lại báo cáo |
| Đỗ Minh Nhật | - Tìm hiểu và lựa chọn bộ dữ liệu<br>- Làm và nộp báo cáo<br>- Tìm hiểu mô hình Vistral-V-7B<br>- Tạo và chạy thử mô hình Vistral-V-7B<br>- Finetune mô hình PaliGemma với Nguyễn Quý Đang<br>- Trực quan hóa kết quả thử nghiệm |
| Vũ Văn Long | - Tìm hiểu về các kỹ thuật tối ưu quá trình huấn luyện mô hình<br>- Xem và hiểu chỉnh phần báo cáo<br>- Viết phần Phụ lục cho báo cáo<br>- Cùng làm demo cho mô hình PaliGemma với Nguyễn Quý đang<br>- Làm slide<br>- Tìm hiểu các cách tiếp cận cổ điển với bài toán VQA đã cho |

[contributors-shield]: https://img.shields.io/github/contributors/dangnq2501/NLP_VQA.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors](https://github.com/dangnq2501/NLP_VQA/graphs/contributorsf)
[forks-shield]: https://img.shields.io/github/forks/dangnq2501/NLP_VQA.svg?style=for-the-badge
[forks-url]: https://github.com/dangnq2501/NLP_VQA/network/members
[stars-shield]: https://img.shields.io/github/stars/dangnq2501/NLP_VQA.svg?style=for-the-badge
[stars-url]: https://github.com/dangnq2501/NLP_VQA/stargazers 
[issues-shield]: https://img.shields.io/github/issues/dangnq2501/NLP_VQA.svg?style=for-the-badge
[issues-url]: https://github.com/dangnq2501/NLP_VQA/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[license-url]: https://github.com/dangnq2501/NLP_VQA/blob/master/LICENSE.md
