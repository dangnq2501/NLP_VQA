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

## Team Memers
- Nguyễn Quý Đang - 22022500 
- Đỗ Minh Nhật - 22022537
- Vũ Vân Long - 22022501

## Phân công công việc


[contributors-shield]: https://img.shields.io/github/contributors/dangnq2501/NLP_VQA.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors](https://github.com/dangnq2501/NLP_VQA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dangnq2501/NLP_VQA.svg?style=for-the-badge
[forks-url]: https://github.com/dangnq2501/NLP_VQA/network/members
[stars-shield]: https://img.shields.io/github/stars/dangnq2501/NLP_VQA.svg?style=for-the-badge
[stars-url]: https://github.com/dangnq2501/NLP_VQA/stargazers 
[issues-shield]: https://img.shields.io/github/issues/dangnq2501/NLP_VQA.svg?style=for-the-badge
[issues-url]: https://github.com/dangnq2501/NLP_VQA/issues
[license-shield]: https://img.shields.io/github/license/dangnq2501/NLP_VQA.svg?style=for-the-badge
[license-url]: https://github.com/dangnq2501/NLP_VQA/blob/master/LICENSE.md
