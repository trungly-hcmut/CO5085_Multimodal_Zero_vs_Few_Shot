# Assignment 1 – Multimodal Classification (Zero-shot vs Few-shot) - CO5085: Học Sâu và Ứng Dụng Trong Thị Giác Máy Tính

---

## Lý thuyết nền tảng

### 1. Mô hình nền tảng: CLIP

**CLIP** (Contrastive Language–Image Pre-training, OpenAI 2021) là mô hình học đa phương thức được huấn luyện trên **400 triệu cặp ảnh–văn bản** từ Internet bằng **contrastive loss**: đẩy embedding ảnh và caption đúng cặp lại gần nhau, các cặp sai xa nhau.

```
              Text Encoder (Transformer)
Caption ────► [ "A dog running on grass" ] ──► text_feat  ─┐
                                                             │ cosine similarity
Image  ─────► [ ViT-B/32 ]                  ──► img_feat  ─┘
```

Kết quả: **một không gian embedding dùng chung** cho cả ảnh lẫn văn bản — cho phép so sánh trực tiếp ảnh với text mà không cần nhãn.

---

### 2. Zero-shot Classification

**Định nghĩa:** Phân loại mà **không dùng bất kỳ mẫu có nhãn nào** để huấn luyện classifier.

**Cách hoạt động với CLIP:**
1. Với mỗi lớp (ví dụ `animals`), tạo câu mô tả: *"a photo mainly about animals"*.
2. Encode câu mô tả đó thành **class prototype** (text embedding).
3. Encode ảnh + caption mẫu cần phân loại thành **query embedding** (image + text fusion).
4. Tính **cosine similarity** giữa query và toàn bộ class prototype.
5. Dự đoán = lớp có similarity cao nhất.

```
query_feat · class_proto[k]
ŷ = argmax ─────────────────────────  (k ∈ {0,...,K-1})
            ‖query_feat‖ · ‖class_proto[k]‖
```

**Ưu điểm:** Không cần dữ liệu huấn luyện, rất linh hoạt.  
**Nhược điểm:** Phụ thuộc vào chất lượng prompt, độ phù hợp giữa tên lớp và ngôn ngữ CLIP đã học.

---

### 3. Few-shot Classification

**Định nghĩa:** Phân loại với **rất ít mẫu có nhãn** (K mẫu mỗi lớp, thường K ∈ {1, 4, 8, 16, 32, 64, 128}).

**Cách hoạt động (Linear Probe trên CLIP features):**
1. Lấy K mẫu mỗi lớp → encode bằng CLIP (ảnh + text) → thu embedding.
2. Dùng embedding đó để huấn luyện **Logistic Regression** (linear classifier).
3. Evaluate trên test set bằng classifier đã học.

```
Embedding (512-dim) ──► LogisticRegression ──► ŷ
      X_fs (K × C mẫu)     (fit nhanh ~ms)    test_acc
```

**Ưu điểm:** Vẫn dùng ít dữ liệu, nhưng học được ranh giới quyết định từ mẫu thật.  
**Nhược điểm:** Cần có K mẫu nhãn thật, nhạy với K nhỏ và mất cân bằng lớp.

---

### 4. Ý nghĩa các Metric đánh giá

| Metric | Công thức | Ý nghĩa |
|--------|-----------|---------|
| **Accuracy** | TP+TN / tổng mẫu | Tỷ lệ đúng tổng thể. Bị ảnh hưởng mạnh bởi lệch lớp. |
| **Precision** (per class) | TP / (TP+FP) | Trong các mẫu được dự đoán là lớp k, bao nhiêu % đúng. |
| **Recall** (per class) | TP / (TP+FN) | Trong các mẫu thật sự là lớp k, mô hình tìm đúng bao nhiêu %. |
| **F1-score** (per class) | 2 · P·R / (P+R) | Trung hòa giữa Precision và Recall. |
| **Macro-F1** | (1/K) Σ F1_k | Trung bình F1 đều nhau qua các lớp. **Công bằng với lớp nhỏ.** |
| **Weighted-F1** | Σ (n_k/N) · F1_k | Trung bình F1 có trọng số theo số mẫu. Phù hợp khi lớp lệch. |

> **Tại sao dùng Macro-F1 cho bài này?**  
> Dataset có lệch lớp (`people` chiếm ~42% train). Nếu chỉ dùng Accuracy, mô hình predict toàn `people` vẫn đạt ~42%. Macro-F1 phạt nặng khi mô hình bỏ qua lớp thiểu số.

---

## Kết quả (mới nhất)

### So sánh chính (Zero-shot vs Few-shot K=64)

| Phương pháp | Accuracy | Macro-F1 |
|-------------|----------|----------|
| Zero-shot (CLIP) | 0.5686 | 0.5030 |
| Few-shot (Linear Probe, K=64) | 0.5574 | **0.5690** |

### Ablation theo K-shot

| K-shot | Train samples | Accuracy | Macro-F1 | Best alpha | Best C | Runtime (s) |
|-------:|--------------:|---------:|---------:|-----------:|-------:|------------:|
| 32 | 256 | 0.5451 | 0.5589 | 0.35 | 5.0 | 8.9 |
| 64 | 512 | 0.5574 | 0.5690 | 0.35 | 10.0 | 8.7 |
| 128 | 1024 | **0.6260** | **0.6171** | 0.35 | 5.0 | 15.3 |

## Phần mở rộng đã thực hiện

- **Interpretability**: image occlusion sensitivity + word ablation importance.
- **Error analysis**: top confusion pairs + high-confidence misclassified samples + giải thích ngắn.
- **K-shot benchmark**: so sánh K=32/64/128 với biểu đồ hiệu năng và thời gian chạy.

## File output quan trọng

- `outputs/multimodal_results.csv`
- `outputs/multimodal_predictions.csv`
- `outputs/report4_metrics.png`
- `outputs/report4_confusion.png`
- `outputs/interpretability_error_cases.png`
- `outputs/error_analysis_notes.csv`
- `outputs/top_confusion_pairs.csv`
- `outputs/kshot_benchmark.csv`
- `outputs/kshot_benchmark.png`

---

- **Dataset**: `AnyModal/flickr30k` (subset dùng trong notebook: train tối đa 8000, test tối đa 2000)  
- **Model**: `openai/clip-vit-base-patch32` (512-dim embedding)  
- **Classes**: animals, indoor, nature, people, sports, transport, urban, water  
- **Device**: MPS (Apple Silicon)
