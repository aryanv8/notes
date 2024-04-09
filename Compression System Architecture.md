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

![[Pasted image 20240409132922.png]]

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
