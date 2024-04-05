It’s a system for image compression that leverages a Transformer-CNN Mixture (TCM) block and a channel-wise entropy model.

1. **Image Compression System**: This is the overall system that takes an input image and produces an output image. It consists of an encoder, a TCM block, an entropy model, and a transmission system.
    
2. **TCM Block**: The TCM block is part of the encoder. It leverages Convolutional Neural Networks (CNNs) for local modeling and transformers for non-local modeling. The input to the TCM block is split into two streams: a CNN stream and a transformer stream. The CNN stream passes through a residual network, while the transformer stream is processed by Swin Transformer blocks. The outputs of both streams are then concatenated and further processed to fuse local and non-local features.
    
3. **Entropy Model**: This model is used for efficient encoding of the image. It introduces a channel-wise auto-regressive entropy model with a SWAtten module. The SWAtten module is a parameter-efficient transformer-based attention mechanism designed for the entropy model. It includes a Swin Transformer block that captures non-local information for improved entropy modeling.
    
4. **Transmission System**: This system is responsible for the transmission of the encoded image. It includes a quantization step, which generates a quantized version of the latent representation of the image. This quantized version is then encoded by a range coder for transmission.
    

Each of these components plays a crucial role in the image compression process. The TCM block and the entropy model work together to efficiently encode the image, capturing both local and non-local features. The transmission system then ensures that this encoded image can be effectively transmitted. The entire system is designed to provide high-quality image compression with efficient use of resources.


1. **Problem Formulation**: The goal of the system is to compress images. The encoder estimates a latent representation (y) with a mean (μ). Quantization is applied to y to generate yˆ for entropy coding. The range coder then efficiently encodes the residuals (y - yˆ) for transmission. The channel-wise entropy model utilizes slice-based processing (y = {y0, …, ys-1}) for improved encoding efficiency.
> 	The notation `{y0, …, ys-1}` indicates that `y` is divided into `s` slices along the channel dimension. Each slice, denoted by `yi` (where `i` ranges from `0` to `s-1`), is processed independently by the entropy model.
    
2. **Transformer-CNN Mixture Blocks (TCM)**: The TCM block is a key component of the system. It combines Convolutional Neural Networks (CNNs) and Swin Transformer (SwinT) blocks to capture both local and non-local image features. The input tensor (F) with size C × HF × WF is processed by a 1x1 convolutional layer to maintain the channel number ©. The tensor is then split into a CNN stream (Fcnn) and a transformer stream (Ftrans) with size C/2 × HF × WF for parallel processing. The CNN stream passes through a residual network to obtain Fcnn, while the transformer stream is processed by SwinT blocks to capture non-local dependencies. The outputs of both streams are then concatenated and further processed by a 1x1 convolutional layer to fuse local and non-local features. A skip connection between the input (F) and output (Fout) improves gradient flow. The TCM block consists of two stages with similar processes but using window-based multi-head self-attention (W-MSA) in stage I and shifted window based multi-head self-attention (SW-MSA) in stage II for the transformer blocks.
    

This system is designed to provide efficient and high-quality image compression by leveraging the strengths of both CNNs and transformers. The channel-wise entropy model and the TCM block work together to efficiently encode the image, capturing both local and non-local features, and the range coder ensures that this encoded image can be effectively transmitted.

In the context of the system you’re describing, `C * HF * WF` represents the dimensions of the input tensor to the Transformer-CNN Mixture (TCM) block. Here’s what each term stands for:

- `C`: The number of channels in the input image. For a grayscale image, `C` would be 1. For a color image in the RGB color space, `C` would be 3.
    
- `HF`: The height of the feature map.
    
- `WF`: The width of the feature map.
    

So, an input tensor with size `C * HF * WF` means that the tensor has `C` channels, each of which is a 2D feature map of size `HF * WF`. This is a common way to represent images in deep learning models.

## Proposed Entropy Model
leverages a Transformer-CNN Mixture (TCM) block and a channel-wise entropy model.

1. **Channel-wise Auto-regressive Entropy Model**: This model is used for efficient encoding of the image. It introduces a channel-wise auto-regressive entropy model with a SWAtten module. The entropy model is auto-regressive, meaning it predicts the next value in a sequence based on the values that came before it. This is done on a channel-wise basis, meaning it’s done separately for each channel of the image.
    
2. **SWAtten**: This is a parameter-efficient Swin Transformer-based attention module designed for the entropy model due to its lower input size. It includes a Swin Transformer block that captures non-local information for improved entropy modeling. The SWAtten module also performs channel squeezing in each slice to balance complexity and performance. The model with SWAtten demonstrates less information loss compared to the model without it, indicating its effectiveness.
    
3. **Combination of Channel-wise Entropy Model with TCM**: The proposed method combines the channel-wise entropy model with the TCM. The TCM blocks extract both local and non-local image features, while the entropy model with SWAtten efficiently encodes residuals for transmission. This combination allows the system to leverage the strengths of both the TCM and the entropy model, resulting in efficient and high-quality image compression.
    

In summary, this system is designed to provide efficient and high-quality image compression by leveraging the strengths of both CNNs and transformers, and by using an efficient entropy model for encoding. The SWAtten module further enhances the performance of the entropy model, resulting in less information loss during the compression process.

