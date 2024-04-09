```mermaid
%% Define graph
graph LR

subgraph ImageCompressionSystem[Image Compression System]
    style ImageCompressionSystem fill:#f9f,stroke:#333,stroke-width:2px;
    A[Input Image]
    B[Encoder]
    C[TCM Block]
    D[Entropy Model]
    E[Output Image]
end

subgraph TCMBlock[TCM Block]
    style TCMBlock fill:#f9f,stroke:#333,stroke-width:2px;
    I[CNN Stream]
    J[Transformer Stream]
    K[Residual Network]
    L[Swin Transformer Blocks]
end

subgraph EntropyModel[Entropy Model]
    style EntropyModel fill:#f9f,stroke:#333,stroke-width:2px;
    M[SWAtten]
    N[Swin Transformer Block]
end

subgraph TransmissionSystem[Transmission System]
    style TransmissionSystem fill:#f9f,stroke:#333,stroke-width:2px;
    F[Quantization]
    G[Range Coder]
    H[Transmission]
end

```

```mermaid
%% Define graph
graph LR

subgraph ImageCompressionSystem[Image Compression System]
    style ImageCompressionSystem fill:#f9f,stroke:#333,stroke-width:2px;
    A[Input Image]
    B[Encoder]
    C[TCM Block]
    D[Entropy Model]
    E[Transmission System]
    F[Decoder]
    G[Output Image]
end

subgraph TCMBlock[TCM Block]
    style TCMBlock fill:#f9f,stroke:#333,stroke-width:2px;
    I[CNN Stream]
    J[Transformer Stream]
    K[Residual Network]
    L[Swin Transformer Blocks]
end

subgraph EntropyModel[Entropy Model]
    style EntropyModel fill:#f9f,stroke:#333,stroke-width:2px;
    M[SWAtten]
    N[Swin Transformer Block]
end

subgraph TransmissionSystem[Transmission System]
    style TransmissionSystem fill:#f9f,stroke:#333,stroke-width:2px;
    O[Quantization]
    P[Range Coder]
    Q[Transmission]
end

```


```mermaid
%% Define graph
graph TB

subgraph ImageCompressionSystem[Image Compression System Architecture]
    style ImageCompressionSystem fill:#f9f,stroke:#333,stroke-width:2px;
    subgraph InputImage[Input Image]
        style InputImage fill:#fff,stroke:#333,stroke-width:2px;
        A[Data Source]
    end
    subgraph Encoder[Encoder]
        style Encoder fill:#fff,stroke:#333,stroke-width:2px;
    end
    subgraph TCMBlock[TCM Block]
        style TCMBlock fill:#fff,stroke:#333,stroke-width:2px;
	    I[CNN Stream]
	    J[Transformer Stream]
	    K[Residual Network]
	    L[Swin Transformer Blocks]
    end
    subgraph EntropyModel[Entropy Model]
        style EntropyModel fill:#fff,stroke:#333,stroke-width:2px;
        M[SWAtten]
	    N[Swin Transformer Block]
    end
    subgraph TransmissionSystem[Transmission System]
        style TransmissionSystem fill:#fff,stroke:#333,stroke-width:2px;
        O[Quantization]
	    P[Range Coder]
	    Q[Transmission]
    end
    subgraph Decoder[Decoder]
        style Decoder fill:#fff,stroke:#333,stroke-width:2px;
        F[Processing]
    end
    subgraph OutputImage[Output Image]
        style OutputImage fill:#fff,stroke:#333,stroke-width:2px;
        G[Data Sink]
    end
end

```

```mermaid
%% Define graph
graph TB

subgraph ImageCompressionSystem[Image Compression System Architecture]
style ImageCompressionSystem align-items:left;
    subgraph InputImage[Input Image]
        style InputImage fill:#fff,stroke:#333,stroke-width:2px;
        A[Data Source]
    end
    subgraph Encoder[Encoder]
        style Encoder fill:#fff,stroke:#333,stroke-width:2px;
    end
    subgraph TCMBlock[TCM Block]
        style TCMBlock fill:#fff,stroke:#333,stroke-width:2px;
	    I[CNN Stream]
	    J[Transformer Stream]
	    K[Residual Network]
	    L[Swin Transformer Blocks]
    end
    subgraph EntropyModel[Entropy Model]
        style EntropyModel fill:#fff,stroke:#333,stroke-width:2px;
        M[SWAtten]
	    N[Swin Transformer Block]
    end
    subgraph TransmissionSystem[Transmission System]
        style TransmissionSystem fill:#fff,stroke:#333,stroke-width:2px;
        O[Quantization]
	    P[Range Coder]
	    Q[Transmission]
    end
    subgraph Decoder[Decoder]
        style Decoder fill:#fff,stroke:#333,stroke-width:2px;
        F[Processing]
    end
    subgraph OutputImage[Output Image]
        style OutputImage fill:#fff,stroke:#333,stroke-width:2px;
        G[Data Sink]
    end
end

```

```mermaid
graph TB

subgraph ImageCompressionSystem[Image Compression System Architecture]
style ImageCompressionSystem fill:#fff,stroke:#333,stroke-width:2px, width:80%;
    subgraph InputImage[Input Image]
        style InputImage fill:#fff,stroke:#333,stroke-width:2px, width:80%;
        A[Data Source]
    end
    subgraph Encoder[Encoder]
        style Encoder fill:#fff,stroke:#333,stroke-width:2px, width:80%;
    end
    subgraph TCMBlock[TCM Block]
        style TCMBlock fill:#fff,stroke:#333,stroke-width:2px, width:80%;
	    I[CNN Stream]
	    J[Transformer Stream]
	    K[Residual Network]
	    L[Swin Transformer Blocks]
    end
    subgraph EntropyModel[Entropy Model]
        style EntropyModel fill:#fff,stroke:#333,stroke-width:2px, width:80%;
        M[SWAtten]
	    N[Swin Transformer Block]
    end
    subgraph TransmissionSystem[Transmission System]
        style TransmissionSystem fill:#fff,stroke:#333,stroke-width:2px, width:80%;
        O[Quantization]
	    P[Range Coder]
	    Q[Transmission]
    end
    subgraph Decoder[Decoder]
        style Decoder fill:#fff,stroke:#333,stroke-width:2px, width:80%;
        F[Processing]
    end
    subgraph OutputImage[Output Image]
        style OutputImage fill:#fff,stroke:#333,stroke-width:2px, width:80%;
        G[Data Sink]
    end
end

```

```mermaid
graph TB
    A[Input Image] --> B[Encoder]
    B -->|Latent Representation y| C[Quantization]
    C -->|yˆ| D[Entropy Coding]
    D -->|Residuals y - yˆ| E[Range Coder]
    E --> F[Transmission]
    B --> G[TCM Block]
    G --> H[CNN Stream]
    G --> I[Transformer Stream]
    H --> J[Residual Network]
    I --> K[Swin Transformer Blocks]
    J --> L[Concatenation]
    K --> L
    L --> M[1x1 Convolutional Layer]
    M --> N[Output Fout]
    A --> O[Channel-wise Entropy Model]
    O --> P[Slice-based Processing]
    P --> Q[SWAtten]
    Q --> R[Swin Transformer Block]
    R --> S[Entropy Model]
    S --> D

```


```mermaid
graph LR
    A[Input Image] --> B[Encoder]
    B --> C[TCM Block]
    C --> D[Entropy Model]
    D --> E[Output Image]
    B --> F[Quantization]
    F --> G[Range Coder]
    G --> H[Transmission]
    C --> I[CNN Stream]
    C --> J[Transformer Stream]
    I --> K[Residual Network]
    J --> L[Swin Transformer Blocks]
    D --> M[SWAtten]
    M --> N[Swin Transformer Block]

```


```mermaid
graph LR
    subgraph "Image Compression System"
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
    end
    subgraph "TCM Block"
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
    end
    subgraph "Entropy Model"
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
    end
    subgraph "Transmission System"
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
    end

```

```mermaid
graph LR
    subgraph "Image Compression System"
        style "Image Compression System" fill:#f2eeee,stroke:#333
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
    end
    subgraph "TCM Block"
        style "TCM Block" fill:#f2eeee,stroke:#333
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
    end
    subgraph "Entropy Model"
        style "Entropy Model" fill:#f2eeee,stroke:#333
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
    end
    subgraph "Transmission System"
        style "Transmission System" fill:#f2eeee,stroke:#333
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
    end

```

```mermaid
graph LR
    subgraph "Image Compression System"
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
    end
    style Image Compression System fill:#f2eeee,stroke:#333
    subgraph "TCM Block"
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
    end
    style TCM Block fill:#f2eeee,stroke:#333
    subgraph "Entropy Model"
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
    end
    style Entropy Model fill:#f2eeee,stroke:#333
    subgraph "Transmission System"
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
    end
    style Transmission System fill:#f2eeee,stroke:#333

```

```mermaid
graph LR
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
    end
    style ImageCompressionSystem fill:#ffcaca,stroke:#333
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
    end
    style TCMBlock fill:#d9edf7,stroke:#333
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
    end
    style EntropyModel fill:#fcf8e3,stroke:#333
    subgraph TransmissionSystem[Transmission System]
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
    end
    style TransmissionSystem fill:#edffdd,stroke:#333

```

# NEW

```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
    end
    subgraph TransmissionSystem[Transmission System]
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
    end

```
```mermaid
%% Use Case Diagram
usecaseDiagram
    participant User
    participant System
    User --> (Compress Image)
    User --> (Decompress Image)
    System --> (Compress Image)
    System --> (Decompress Image)
```

```mermaid
%% Class Diagram
classDiagram
    class AnalysisTransform
    class SynthesisTransform
    class HyperAnalysisTransform
    class HyperSynthesisTransform
    class AttentionBlock
    class SWAtten
    class ConvolutionalBlocks
    class Config
    class UtilityFunctions

    AnalysisTransform <|-- SynthesisTransform
    HyperAnalysisTransform <|-- HyperSynthesisTransform
    AttentionBlock <|-- SWAtten
    ConvolutionalBlocks <|-- ResidualBlock
    ConvolutionalBlocks <|-- ResidualBlockWithStride
    ConvolutionalBlocks <|-- ResidualBlockUpsample
```

```mermaid
%% Sequence Diagram
sequenceDiagram
    participant User
    participant System
    User ->> System: Input Image
    System ->> System: Compress Image
    System ->> System: Decompress Image
    System -->> User: Output Image

```


# Copilot Answer

### Data Flow Diagram
```mermaid
graph LR
    A[Input Image] --> B[Encoder]
    B --> C[TCM Block]
    C --> D[Entropy Model]
    D --> E[Output Image]
    B --> F[Quantization]
    F --> G[Range Coder]
    G --> H[Transmission]

```

```mermaid
graph TD
    A[Input Image] -->|Input| B[Encoder]
    B -->|Estimates Latent Representation #40;y#41;| C[AnalysisTransform]
    C -->|Applies TCM| D[TCM Block]
    D -->|Feature Fusion| E[Entropy Model]
    E -->|SWAtten Module| F[SWAtten]
    F -->|Encoded Image| G[Output Image]
    G -->|Decompression| H[SynthesisTransform]
    H -->|Reconstructed Image| I[Output]

    B -->|Quantization| J[Quantization]
    J -->|Range Coding| K[Range Coder]
    K -->|Transmission| L[Transmission System]
```

```mermaid
graph TD
    A[Input Image] -->|Input| B[Encoder]
    B -->|Estimates Latent Representation #40;y#41;| C[AnalysisTransform]
    C -->|Applies TCM| D[TCM Block]
    D -->|Quantization| E[Quantization]
    E -->|Feature Fusion| F[Entropy Model]
    F -->|SWAtten Module| G[SWAtten]
    G -->|Encoded Image| H[Output Image]
    H -->|Decompression| I[SynthesisTransform]
    I -->|Reconstructed Image| J[Output]

    style A fill:#f9f,stroke:#333
    style B fill:#fcf,stroke:#333
    style C fill:#cff,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#ff9,stroke:#333
    style F fill:#9ff,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#f9f,stroke:#333

```


```mermaid
graph TD
    A[Input Image] -->|Input| B[Encoder]
    B -->|Latent Representation| C[AnalysisTransform]
    C -->|Applies TCM| D[TCM Block]
    D -->|Quantization| E[Quantization]
    E -->|Feature Fusion| F[Entropy Model]
    F -->|SWAtten Module| G[SWAtten]
    G -->|Encoded Image| H[Output Image]
    H -->|Decompression| I[SynthesisTransform]
    I -->|Reconstructed Image| J[Output]

    style A fill:#f9f,stroke:#333
    style B fill:#fcf,stroke:#333
    style C fill:#cff,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#ff9,stroke:#333
    style F fill:#9ff,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#f9f,stroke:#333

```

```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

    B-->C
    C-->F
    F-->G
    G-->H

```




```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        B --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

    B-->C
    C-->F
    F-->G
    G-->H

```


```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> P[Decoder]
        P --> E[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        C --> F[Quantization]
        F --> G[Range Coder]
        G --> H[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end


```



```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
    
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        C --> F[Quantization]
        F --> |Encoded Data| G[Range Coder]
        G --> |Compressed Data| H[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

```


```mermaid
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] -->|Input| B[Encoder]
        B -->|Estimates Latent Representation| C[TCM Block]
        C -->|Applies TCM| D[Entropy Model]
        D -->|Feature Fusion| E[Decoder]
        E -->|Decompressed Image| F[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C -->|CNN Stream| I[Residual Network]
        C -->|Transformer Stream| J[Swin Transformer Blocks]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D -->|SWAtten Module| M[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        C -->|Quantization| F[Range Coder]
        F -->|Encoded Data| G[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

```



```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B[Encoder]
        B --> C[TCM Block]
        C --> D[Entropy Model]
        D --> E[Decoder]
        E --> F[Output Image]
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        C --> O[Quantization]
        O --> P[Range Coder]
        P --> Q[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

    B-->C
    D-->E
    O-->|Encoded Data| P[Range Coder]
    P-->|Compressed Data| Q[Transmission]

```



```mermaid
%% Data Flow Diagram
graph TD
    subgraph ImageCompressionSystem[Image Compression System]
        A[Input Image] --> B((Encoder))
        D[Output Image] --> P((Decoder))
        style ImageCompressionSystem fill:#ffcaca,stroke:#333
    end
    subgraph TCMBlock[TCM Block]
        B --> C{Split F}
        C --> I[CNN Stream]
        C --> J[Transformer Stream]
        I --> K[Residual Network]
        J --> L[Swin Transformer Blocks]
        C --> F[Quantization]
        style TCMBlock fill:#d9edf7,stroke:#333
    end
    subgraph EntropyModel[Entropy Model]
        C --> D[Entropy Model]
        D --> M[SWAtten]
        M --> N[Swin Transformer Block]
        style EntropyModel fill:#fcf8e3,stroke:#333
    end
    subgraph TransmissionSystem[Transmission System]
        F --> G[Range Coder]
        G --> H[Transmission]
        style TransmissionSystem fill:#edffdd,stroke:#333
    end

    %% External Entities
    InputImage((Input Image))
    OutputImage((Output Image))

    %% Processes
    Encoder((Encoder))
    Decoder((Decoder))
    Quantization((Quantization))
    RangeCoder((Range Coder))
    Transmission((Transmission))

    %% Data Stores
    SWAtten((SWAtten))
    ResidualNetwork((Residual Network))
    SwinTransformer((Swin Transformer Blocks))

    %% Data Flows
    InputImage --> Encoder
    Encoder --> TCMBlock
    TCMBlock --> Quantization
    Quantization --> RangeCoder
    RangeCoder --> Transmission
    Transmission --> OutputImage
    SWAtten --> EntropyModel
    ResidualNetwork --> TCMBlock
    SwinTransformer --> TCMBlock

```



```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        Decoder((Decoder))
        Quantization((Quantization))
        RangeCoder((Range Coder))
        Transmission((Transmission))
    end

    subgraph DataStores
        SWAtten((SWAtten))
        ResidualNetwork((Residual Network))
        SwinTransformer((Swin Transformer Blocks))
    end

    InputImage --> Encoder
    Encoder --> Quantization
    Quantization --> RangeCoder
    RangeCoder --> Transmission
    Transmission --> OutputImage

    Encoder --> TCMBlock
    TCMBlock --> Decoder
    TCMBlock --> SWAtten
    SWAtten --> EntropyModel
    TCMBlock --> ResidualNetwork
    TCMBlock --> SwinTransformer

```


```mermaid
graph LR
  subgraph Input[Input]
    A[Image] --> B(Encode)
  end

  subgraph TCM[TCM Block]
    B --> C(Extract Features)
    C --> D(Split Stream)
    D --> E(CNN Stream)
    D --> F(Transformer Stream)
    E --> G(Residual Network)
    F --> H(Swin Transformer)
    G --> I{Local Features}
	H --> I{Non-Local Features}

    I --> J(Concatenate)
  end

  subgraph Entropy[Entropy Model]
    C --> K(Channel-wise Entropy)
    K --> L(SWAtten)
    L --> M(Swin Transformer)
    M --> N(Residuals)
  end

  subgraph Transmission[Transmission Channel]
    C --> O(Quantization)
    O --> P(Range Coding)
    P --> Q(Transmission)
  end

  subgraph Output[Output]
    N --> R(Decode)
    R --> S(Image)
  end
```



```mermaid
graph LR
  subgraph Input[Input]
    A[Image] --> B(Encode)
  end

  subgraph TCM[TCM Block]
    B --> C(Extract Features)
    C --> D(Split Stream)
    D --> E(CNN Stream)
    D --> F(Transformer Stream)
    E --> G(Residual Network)
    F --> H(Swin Transformer)
    G --> I{Local Features}
    H --> I{Non-Local Features}
    I --> J(Concatenate)
    J --> C(Feature Map)  
  end

  subgraph Entropy[Entropy Model]
    C --> K(Channel-wise Entropy)
    K --> L(SWAtten)
    L --> M(Swin Transformer)
    M --> N(Residuals)
  end

  subgraph Transmission[Transmission Channel]
    C --> O(Quantization)
    O --> P(Range Coding)
    P --> Q(Transmission)
  end

  subgraph Output[Output]
    N --> R(Decode)
    R --> S(Image)
  end

```

```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        Quantization((Quantization))
        RangeCoder((Range Coder))
        Transmission((Transmission))
        Decoder((Decoder))
    end

    subgraph DataStores
        SWAtten((SWAtten))
        ResidualNetwork((Residual Network))
        SwinTransformer((Swin Transformer Blocks))
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| Quantization
    Quantization -->|Quantized Image| RangeCoder
    RangeCoder -->|Compressed Image| Transmission
    Transmission -->|Transmitted Image| OutputImage

    Encoder -->|Encoded Image| TCMBlock
    TCMBlock -->|Decoded Image| Decoder
    TCMBlock -->|SWAtten Data| SWAtten
    SWAtten -->|Entropy Model| Quantization
    TCMBlock -->|Residual Data| ResidualNetwork
    TCMBlock -->|Transformer Data| SwinTransformer

```

```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        Quantization((Quantization))
        RangeCoder((Range Coder))
        Transmission((Transmission))
        SWAtten((SWAtten))
        Decoder((Decoder))
    end

    subgraph DataStores
        ResidualNetwork((Residual Network))
        SwinTransformer((Swin Transformer Blocks))
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| Quantization
    Quantization -->|Quantized Image| RangeCoder
    RangeCoder -->|Compressed Image| Transmission
    Transmission -->|Transmitted Image| OutputImage

    Encoder -->|Encoded Image| TCMBlock
    TCMBlock -->|SWAtten Data| SWAtten
    SWAtten -->|Entropy Model| Quantization
    TCMBlock -->|Residual Data| ResidualNetwork
    TCMBlock -->|Transformer Data| SwinTransformer
    SwinTransformer -->|Decoded Image| Decoder

```


```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        Quantization((Quantization))
        RangeCoder((Range Coder))
        Transmission((Transmission))
        SWAtten((SWAtten))
        Decoder((Decoder))
    end

    subgraph DataStores
        ResidualNetwork((Residual Network))
        SwinTransformer((Swin Transformer Blocks))
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| TCMBlock
    TCMBlock -->|SWAtten Data| SWAtten
    SWAtten -->|Entropy Model| Quantization
    TCMBlock -->|Residual Data| ResidualNetwork
    TCMBlock -->|Transformer Data| SwinTransformer
    SwinTransformer -->|Decoded Image| Decoder
    Decoder -->|Decoded Image| OutputImage

```


```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        TCM((TCM))
        Entropy((Entropy Model))
        Decoder((Decoder))
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| TCM
    TCM -->|Processed Image| Entropy
    Entropy -->|Entropy Encoded Image| Decoder
    Decoder -->|Decoded Image| OutputImage

```

```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        TCM[TCM]
        Entropy[Entropy Model]
        Decoder((Decoder))
    end

    subgraph TCM
        TCMSteps[1. TCM processing]
    end

    subgraph Entropy
        SWAttn((SWAttn))
        EntropySteps[2. Entropy Encoding]
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| TCMSteps
    TCMSteps -->|Processed Image| EntropySteps
    EntropySteps -->|Entropy Encoded Image| Decoder
    Decoder -->|Decoded Image| OutputImage

```


```mermaid
%% Data Flow Diagram
graph TD
    subgraph ExternalEntities
        InputImage((Input Image))
        OutputImage((Output Image))
    end

    subgraph Processes
        Encoder((Encoder))
        TCM[TCM Block]
        Entropy[Entropy Model]
        Decoder((Decoder))
    end

    subgraph TCM
        I[CNN Stream]
        J[Transformer Stream]
        K[Residual Network]
        L[Swin Transformer Blocks]
    end

    subgraph Entropy
        M[SWAtten]
        N[Swin Transformer Block]
    end

    InputImage --> Encoder
    Encoder -->|Encoded Image| TCM
    TCM -->|Processed Image| Entropy
    Entropy -->|Entropy Encoded Image| Decoder
    Decoder -->|Decoded Image| OutputImage

```





```
  A --> B
  B --> C
  C --> D
  D --> E
  D --> F
  E --> G
  F --> H
  G --> I
  H --> I
  C --> K
  K --> L
  L --> M
  M --> N
  C --> O
  O --> P
  P --> Q
  N --> R
  R --> S
```

```
  Input --> TCM
  TCM --> Entropy
  TCM --> Transmission
  Entropy --> Output
  Transmission --> [External Entity]
```

```
    style A fill:#f9f,stroke:#333
    style B fill:#fcf,stroke:#333
    style C fill:#cff,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#ff9,stroke:#333
    style F fill:#9ff,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#fcf,stroke:#333
    style K fill:#cff,stroke:#333
    style L fill:#cfc,stroke:#333

```
### Use Case Diagram
```mermaid
graph LR
    User((User)) -->|Inputs Image| A[Input Image]
    System((System)) -->|Encodes Image| B[Encoder]
    System -->|Applies TCM| C[TCM Block]
    System -->|Applies Entropy Model| D[Entropy Model]
    System -->|Outputs Image| E[Output Image]

```

#### 2
```mermaid
graph LR
    User((User)) -->|Inputs Image| A[Input Image]
    System((System)) -->|Encodes Image| B[Encoder]
    System -->|Applies TCM Block| C[TCM Block]
    System -->|Applies Entropy Model| D[Entropy Model]
    System -->|Quantizes Latent Representation| E[Quantization]
    System -->|Encodes Residuals| F[Range Coder]
    System -->|Transmits Encoded Data| G[Transmission]
    System -->|Outputs Image| H[Output Image]

```

![[Pasted image 20240409144122.png]]

### Class Diagram

```mermaid
classDiagram
    class ImageCompressionSystem{
        +Input Image
        +Encoder
        +TCM Block
        +Entropy Model
        +Output Image
    }
    class TCMBlock{
        +CNN Stream
        +Transformer Stream
        +Residual Network
        +Swin Transformer Blocks
    }
    class EntropyModel{
        +SWAtten
        +Swin Transformer Block
    }
    class TransmissionSystem{
        +Quantization
        +Range Coder
        +Transmission
    }

```

#### 2

```mermaid
classDiagram
    class ImageCompressionSystem{
        +Input Image
        +Encoder
        +TCM Block
        +Entropy Model
        +Output Image
    }
    class Encoder{
        +AnalysisTransform
        +HyperAnalysisTransform
    }
    class TCMBlock{
        +CNN Stream
        +Transformer Stream
        +Residual Network
        +Swin Transformer Blocks
    }
    class CNNStream{
        +ConvTransBlock
        +ResidualBlock
        +ResidualBlockWithStride
        +ResidualBlockUpsample
    }
    class TransformerStream{
        +Swin Transformer Blocks
    }
    class EntropyModel{
        +SWAtten
        +Swin Transformer Block
    }
    class SWAtten{
        +Channel Squeezing
        +Spatial Relationships
    }
    class TransmissionSystem{
        +Quantization
        +Range Coder
        +Transmission
    }
    ImageCompressionSystem --> Encoder
    ImageCompressionSystem --> TCMBlock
    ImageCompressionSystem --> EntropyModel
    ImageCompressionSystem --> TransmissionSystem
    TCMBlock --> CNNStream
    TCMBlock --> TransformerStream
    EntropyModel --> SWAtten

```

### Sequence Diagram
```mermaid
sequenceDiagram
    participant User as User
    participant System as System
    User->>System: Input Image
    System->>System: Encode Image
    System->>System: Apply TCM
    System->>System: Apply Entropy Model
    System->>User: Output Image

```


```mermaid
sequenceDiagram
    participant User
    participant InputImage as Input Image
    participant Encoder
    participant AnalysisTransform as Analysis Transform
    participant TCMBlock as TCM Block
    participant EntropyModel as Entropy Model
    participant SWAtten
    participant OutputImage as Output Image
    participant SynthesisTransform as Synthesis Transform

    User->>InputImage: Provides
    InputImage->>Encoder: Input
    Encoder->>AnalysisTransform: Encodes to Latent Representation (y)
    AnalysisTransform->>TCMBlock: Applies TCM
    TCMBlock->>EntropyModel: Feature Fusion
    EntropyModel->>SWAtten: Applies SWAtten Module
    SWAtten->>OutputImage: Encoded Image
    OutputImage->>SynthesisTransform: Decompression
    SynthesisTransform->>User: Reconstructed Image

    rect rgb(255, 235, 235)
    note over Encoder, SWAtten: Encoding Process
    end

    rect rgb(235, 255, 235)
    note over SynthesisTransform: Decoding Process
    end

```
