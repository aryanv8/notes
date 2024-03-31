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

