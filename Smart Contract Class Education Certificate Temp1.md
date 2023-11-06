```mermaid
graph TD

subgraph Users
    subgraph Student
        S(Student)
    end
    subgraph Institution
        I(Institution)
    end
    subgraph Government
        G(Government)
    end
    subgraph Verifiers
        V(Verifiers)
    end
end

subgraph Smart Contract
    subgraph Certificate Storage
        CRUD(CRUD Operations)
    end
    subgraph Government Actions
        ModifyEligibility(Modify Eligibility)
    end
    subgraph Institution Actions
        GenerateCertificate(Generate Certificate)
    end
    subgraph Verifier Actions
        VerifyCertificate(Verify Certificate)
    end
    subgraph ML Model
        FeatureExtraction(Feature Extraction)
        PredictJobSuitability(Predict Job Suitability)
        MapEmployerToStudent(Map Employer to Student)
    end
end

S --> CRUD
I --> CRUD
G --> ModifyEligibility
I --> GenerateCertificate
V --> VerifyCertificate
ML_Model --> FeatureExtraction
ML_Model --> PredictJobSuitability
ML_Model --> MapEmployerToStudent

```


```mermaid
graph LR

subgraph Users
    subgraph Student
        S(Student)
    end
    subgraph Institution
        I(Institution)
    end
    subgraph Government
        G(Government)
    end
    subgraph Employer
		    R(Recruiters)
		end
    subgraph Verifiers
        V(Verifiers)
    end
end

subgraph Frontend
    StudentUI(Frontend for Students)
    InstitutionUI(Frontend for Institutions)
    GovernmentUI(Frontend for Government)
    EmployerUI(Frontend for Employer)
    VerifierUI(Frontend for Verifiers)
end

subgraph Backend
    subgraph SmartContract
        subgraph CertificateStorage
            CRUD(CRUD Operations)
        end
        subgraph GovernmentActions
            ModifyEligibility(Modify Eligibility)
        end
        subgraph InstitutionActions
            GenerateCertificate(Generate Certificate)
        end
        subgraph VerifierActions
            VerifyCertificate(Verify Certificate)
        end
        subgraph MLModel
            FeatureExtraction(Feature Extraction)
            PredictJobSuitability(Predict Job Suitability)
            MapEmployerToStudent(Map Employer to Student)
        end
    end
    BC(Blockchain)
    DB(Database)
end

subgraph ExternalServices
    OCR(OCR Service)
    BlockchainOracle(Blockchain Oracle)
end

Student --> StudentUI
Institution --> InstitutionUI
Government --> GovernmentUI
Employer --> EmployerUI
Verifiers --> VerifierUI

StudentUI --> CRUD
InstitutionUI --> GenerateCertificate
GovernmentUI --> ModifyEligibility
VerifierUI --> VerifyCertificate

CRUD --> BC
GenerateCertificate --> BC
VerifyCertificate --> BC
FeatureExtraction --> MLModel
PredictJobSuitability --> MLModel
MapEmployerToStudent --> MLModel

OCR --> DB
OCR --> GenerateCertificate
BlockchainOracle --> BC

```


```mermaid
graph TD

subgraph Users
    subgraph Student
        S(Student)
    end
    subgraph Institution
        I(Institution)
    end
    subgraph Government
        G(Government)
    end
    subgraph Verifiers
        V(Verifiers)
    end
    subgraph Recruiters
        R(Recruiters)
    end
end

subgraph Frontend
    subgraph StudentUI
        StudentUI(Frontend for Students)
    end
    subgraph InstitutionUI
        InstitutionUI(Frontend for Institutions)
    end
    subgraph GovernmentUI
        GovernmentUI(Frontend for Government)
    end
    subgraph VerifierUI
        VerifierUI(Frontend for Verifiers)
    end
    subgraph RecruiterUI
        RecruiterUI(Frontend for Recruiters)
    end
end

subgraph Backend
    subgraph SmartContract
        subgraph CertificateStorage
            CRUD(CRUD Operations)
        end
        subgraph GovernmentActions
            ModifyEligibility(Modify Eligibility)
        end
        subgraph InstitutionActions
            GenerateCertificate(Generate Certificate)
        end
        subgraph VerifierActions
            VerifyCertificate(Verify Certificate)
        end
        subgraph RecruiterActions
            PostJobCriteria(Post Job Criteria)
            PredictStudents(Predict Students)
        end
        subgraph MLModel
            FeatureExtraction(Feature Extraction)
            PredictJobSuitability(Predict Job Suitability)
            MapEmployerToStudent(Map Employer to Student)
        end
    end
    subgraph BlockchainNetwork
        BC(Blockchain)
    end
    subgraph Database
        DB(Database)
    end
end

subgraph ExternalServices
    OCR(OCR Service)
    BlockchainOracle(Blockchain Oracle)
end

Student --> StudentUI
Institution --> InstitutionUI
Government --> GovernmentUI
Verifiers --> VerifierUI
Recruiters --> RecruiterUI

StudentUI --> CRUD
InstitutionUI --> GenerateCertificate
GovernmentUI --> ModifyEligibility
VerifierUI --> VerifyCertificate
RecruiterUI --> PostJobCriteria
RecruiterUI --> PredictStudents

CRUD --> BC
GenerateCertificate --> BC
VerifyCertificate --> BC
PostJobCriteria --> PredictStudents
PredictStudents --> DB
FeatureExtraction --> MLModel
PredictJobSuitability --> MLModel
MapEmployerToStudent --> MLModel

OCR --> DB
OCR --> GenerateCertificate
BlockchainOracle --> BC

```
