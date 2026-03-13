#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo PDF gợi ý Dataset cho Bài tập lớn 1
Môn: Học sâu và ứng dụng trong thị giác máy tính
"""

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # Add Unicode font
        self.add_font('DejaVu', '', '/System/Library/Fonts/Supplemental/Arial Unicode.ttf', uni=True)
        self.add_font('DejaVu', 'B', '/System/Library/Fonts/Supplemental/Arial Unicode.ttf', uni=True)
    
    def header(self):
        self.set_font('DejaVu', 'B', 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, 'Gợi ý Dataset - Bài tập lớn số 1', border=False, ln=True, align='C')
        self.set_font('DejaVu', '', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Môn: Học sâu và ứng dụng trong thị giác máy tính (CO5085)', ln=True, align='C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Trang {self.page_no()}', align='C')
    
    def section_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.set_fill_color(0, 102, 204)
        self.set_text_color(255, 255, 255)
        self.cell(0, 8, f'  {title}', ln=True, fill=True)
        self.ln(3)
        self.set_text_color(0, 0, 0)
    
    def sub_title(self, title):
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(0, 102, 153)
        self.cell(0, 7, title, ln=True)
        self.set_text_color(0, 0, 0)
    
    def add_table(self, headers, data, col_widths):
        # Header
        self.set_font('DejaVu', 'B', 9)
        self.set_fill_color(230, 230, 230)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 7, header, border=1, fill=True, align='C')
        self.ln()
        
        # Data
        self.set_font('DejaVu', '', 8)
        for row in data:
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 6, str(cell), border=1, align='C')
            self.ln()
        self.ln(3)

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # ==================== YÊU CẦU DATASET ====================
    pdf.section_title('1. YÊU CẦU VỀ DATASET (theo đề bài)')
    pdf.set_font('DejaVu', '', 9)
    requirements = [
        "• Số lớp: Ít nhất 5 lớp cho mỗi tập (ảnh, văn bản, đa phương thức)",
        "• Kích thước: Tập huấn luyện ít nhất 5,000 mẫu trở lên",
        "• Độ khó: Ưu tiên tập có độ phân biệt lớp vừa phải trở lên",
        "• Đa phương thức: Phải có cặp ảnh-văn bản thực sự (không ghép ngẫu nhiên)"
    ]
    for req in requirements:
        pdf.cell(0, 5, req, ln=True)
    pdf.ln(5)
    
    # ==================== IMAGE DATASETS ====================
    pdf.section_title('2. IMAGE CLASSIFICATION DATASETS')
    
    image_headers = ['Dataset', 'Số lớp', 'Kích thước', 'Độ khó', 'Nguồn']
    image_data = [
        ['CIFAR-100', '100', '60K ảnh', '⭐⭐⭐', 'torchvision'],
        ['Food-101', '101', '101K ảnh', '⭐⭐⭐', 'Kaggle'],
        ['Stanford Dogs', '120', '20K ảnh', '⭐⭐⭐', 'Stanford'],
        ['Flowers-102', '102', '8K ảnh', '⭐⭐', 'Oxford'],
        ['EuroSAT', '10', '27K ảnh', '⭐⭐', 'GitHub'],
        ['Intel Image', '6', '25K ảnh', '⭐⭐', 'Kaggle'],
        ['Caltech-256', '256', '30K ảnh', '⭐⭐⭐', 'Caltech'],
        ['Tiny ImageNet', '200', '100K ảnh', '⭐⭐⭐⭐', 'Stanford'],
        ['Oxford-IIIT Pets', '37', '7K ảnh', '⭐⭐', 'Oxford'],
        ['FGVC Aircraft', '100', '10K ảnh', '⭐⭐⭐', 'Oxford'],
    ]
    pdf.add_table(image_headers, image_data, [40, 20, 30, 25, 30])
    
    pdf.sub_title('Links tải dataset ảnh:')
    pdf.set_font('DejaVu', '', 8)
    image_links = [
        "• CIFAR-100: pytorch.org/vision/stable/datasets.html",
        "• Food-101: kaggle.com/datasets/dansbecker/food-101",
        "• Stanford Dogs: vision.stanford.edu/aditya86/ImageNetDogs/",
        "• Flowers-102: robots.ox.ac.uk/~vgg/data/flowers/102/",
        "• EuroSAT: github.com/phelber/eurosat",
        "• Intel Image: kaggle.com/datasets/puneet6060/intel-image-classification",
        "• Tiny ImageNet: cs231n.stanford.edu/tiny-imagenet-200.zip"
    ]
    for link in image_links:
        pdf.cell(0, 4, link, ln=True)
    pdf.ln(3)
    
    # ==================== TEXT DATASETS ====================
    pdf.section_title('3. TEXT CLASSIFICATION DATASETS')
    
    text_headers = ['Dataset', 'Số lớp', 'Kích thước', 'Mô tả', 'Nguồn']
    text_data = [
        ['AG News', '4', '120K', 'Tin tức', 'HuggingFace'],
        ['20 Newsgroups', '20', '18K', 'Diễn đàn', 'sklearn'],
        ['DBpedia', '14', '560K', 'Wikipedia', 'HuggingFace'],
        ['Yahoo Answers', '10', '1.4M', 'Q&A', 'HuggingFace'],
        ['Yelp Review Full', '5', '650K', 'Đánh giá', 'HuggingFace'],
        ['GoEmotions', '27', '58K', 'Cảm xúc', 'HuggingFace'],
        ['Banking77', '77', '13K', 'Intent', 'HuggingFace'],
        ['CLINC150', '150', '22.5K', 'Intent', 'HuggingFace'],
        ['Amazon Review', '5', '3M+', 'Sản phẩm', 'HuggingFace'],
        ['TREC', '6', '6K', 'Câu hỏi', 'HuggingFace'],
    ]
    pdf.add_table(text_headers, text_data, [35, 20, 25, 30, 30])
    
    pdf.sub_title('Links tải dataset văn bản:')
    pdf.set_font('DejaVu', '', 8)
    text_links = [
        "• AG News: huggingface.co/datasets/ag_news",
        "• 20 Newsgroups: scikit-learn.org/stable/datasets/real_world.html",
        "• DBpedia: huggingface.co/datasets/dbpedia_14",
        "• Yahoo Answers: huggingface.co/datasets/yahoo_answers_topics",
        "• Yelp Review: huggingface.co/datasets/yelp_review_full",
        "• GoEmotions: huggingface.co/datasets/go_emotions",
        "• Banking77: huggingface.co/datasets/banking77"
    ]
    for link in text_links:
        pdf.cell(0, 4, link, ln=True)
    
    # New page for multimodal
    pdf.add_page()
    
    # ==================== MULTIMODAL DATASETS ====================
    pdf.section_title('4. MULTIMODAL DATASETS (Ảnh + Văn bản)')
    
    multi_headers = ['Dataset', 'Mô tả', 'Kích thước', 'Nguồn']
    multi_data = [
        ['Flickr30k', 'Ảnh + caption', '31K ảnh', 'Kaggle'],
        ['COCO Captions', 'Ảnh + caption', '330K ảnh', 'cocodataset.org'],
        ['Hateful Memes', 'Phân loại meme độc hại', '10K', 'Meta AI'],
        ['Fakeddit', 'Fake news detection', '1M', 'GitHub'],
        ['MM-IMDb', 'Phân loại thể loại phim', '26K', 'GitHub'],
        ['Visual News', 'Tin tức + ảnh', '1M+', 'GitHub'],
        ['SNLI-VE', 'Visual entailment', '565K', 'GitHub'],
        ['VQA v2', 'Visual Q&A', '1.1M Q', 'visualqa.org'],
    ]
    pdf.add_table(multi_headers, multi_data, [35, 50, 30, 30])
    
    pdf.sub_title('Links tải dataset đa phương thức:')
    pdf.set_font('DejaVu', '', 8)
    multi_links = [
        "• Flickr30k: kaggle.com/datasets/hsankesara/flickr-image-dataset",
        "• COCO: cocodataset.org/#download",
        "• Hateful Memes: ai.facebook.com/datasets/hateful-memes",
        "• Fakeddit: github.com/entitize/Fakeddit",
        "• MM-IMDb: github.com/johnarevalo/gmu-mmimdb",
        "• Visual News: github.com/FuxiaoLiu/VisualNews-Repository"
    ]
    for link in multi_links:
        pdf.cell(0, 4, link, ln=True)
    pdf.ln(5)
    
    # ==================== GỢI Ý COMBO ====================
    pdf.section_title('5. GỢI Ý COMBO DATASET')
    
    pdf.sub_title('Option 1: Dễ bắt đầu (Recommended cho người mới)')
    pdf.set_font('DejaVu', '', 9)
    combo1 = [
        "• Ảnh: CIFAR-100 - Nhỏ gọn, dễ train, có sẵn trong torchvision",
        "• Văn bản: AG News hoặc 20 Newsgroups - Phổ biến, nhiều tutorial",
        "• Multimodal: Flickr30k - Dataset cổ điển, nhiều hướng dẫn"
    ]
    for item in combo1:
        pdf.cell(0, 5, item, ln=True)
    pdf.ln(3)
    
    pdf.sub_title('Option 2: Thú vị hơn (Balanced)')
    combo2 = [
        "• Ảnh: Food-101 - Visual đẹp, thực tế, 101 loại món ăn",
        "• Văn bản: GoEmotions - 27 loại cảm xúc, multi-label",
        "• Multimodal: Hateful Memes - Challenging, bài toán thực tế"
    ]
    for item in combo2:
        pdf.cell(0, 5, item, ln=True)
    pdf.ln(3)
    
    pdf.sub_title('Option 3: Challenging (Điểm cao tiềm năng)')
    combo3 = [
        "• Ảnh: Tiny ImageNet - 200 lớp, độ khó cao",
        "• Văn bản: CLINC150 - 150 intents, fine-grained classification",
        "• Multimodal: MM-IMDb - Multi-label movie genre prediction"
    ]
    for item in combo3:
        pdf.cell(0, 5, item, ln=True)
    pdf.ln(5)
    
    # ==================== CODE MẪU ====================
    pdf.section_title('6. CODE MẪU LOAD DATASET')
    
    pdf.sub_title('Load CIFAR-100 (PyTorch):')
    pdf.set_font('Courier', '', 8)
    code1 = """from torchvision import datasets, transforms
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))
])
train_data = datasets.CIFAR100(root='./data', train=True, 
                               download=True, transform=transform)"""
    for line in code1.split('\n'):
        pdf.cell(0, 4, line, ln=True)
    pdf.ln(3)
    
    pdf.sub_title('Load AG News (HuggingFace):')
    code2 = """from datasets import load_dataset
dataset = load_dataset("ag_news")
train_data = dataset["train"]
test_data = dataset["test"]"""
    for line in code2.split('\n'):
        pdf.cell(0, 4, line, ln=True)
    pdf.ln(3)
    
    pdf.sub_title('Load Flickr30k với CLIP:')
    code3 = """from datasets import load_dataset
import clip
model, preprocess = clip.load("ViT-B/32")
dataset = load_dataset("nlphuji/flickr30k")"""
    for line in code3.split('\n'):
        pdf.cell(0, 4, line, ln=True)
    
    # ==================== LƯU Ý ====================
    pdf.ln(5)
    pdf.section_title('7. LƯU Ý QUAN TRỌNG')
    pdf.set_font('DejaVu', '', 9)
    notes = [
        "1. Kiểm tra kỹ số lớp và số mẫu trước khi chọn dataset",
        "2. Nên trao đổi với giảng viên nếu không chắc dataset hợp lệ",
        "3. Ghi rõ lý do chọn dataset trong báo cáo",
        "4. Dataset đa phương thức phải có cặp ảnh-văn bản thực sự",
        "5. Tránh dataset quá đơn giản như MNIST, binary classification"
    ]
    for note in notes:
        pdf.cell(0, 6, note, ln=True)
    
    # Save PDF
    output_path = '/Users/lyminhtrung/Library/CloudStorage/OneDrive-hcmut.edu.vn/DL-CV/Dataset_Suggestions_BTL1.pdf'
    pdf.output(output_path)
    print(f"PDF đã được tạo thành công: {output_path}")

if __name__ == "__main__":
    create_pdf()
