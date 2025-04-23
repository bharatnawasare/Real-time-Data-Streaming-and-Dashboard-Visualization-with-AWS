
<img width="1000" alt="Screenshot 2025-03-12 at 12 18 52 PM" src="https://github.com/user-attachments/assets/53903dbb-d094-43ab-b6c2-3f63a7be4835" />

This repository demonstrates a comprehensive end-to-end solution for ingesting, processing, and visualizing real-time data streams utilizing Amazon Web Services (AWS).

## AWS System Architecture Overview

![lab1arch](https://github.com/user-attachments/assets/448b8ece-306f-48e6-8a54-d75f7bf4b611)

## Project Description

The project leverages AWS to simulate real-time streaming data using the Kinesis Data Generator (KDG). Streaming data is ingested via Amazon Kinesis Data Streams, processed with Amazon Managed Apache Flink using Studio Notebooks (Apache Zeppelin), formatted and buffered through Amazon Kinesis Data Firehose (with a 30-second buffer interval), stored in Amazon S3, cataloged with AWS Glue, queried through Amazon Athena, and finally visualized using Amazon QuickSight.

## AWS Services Utilized
- **Amazon Kinesis Data Streams**: Real-time data ingestion.
- **Amazon Managed Apache Flink (Apache Zeppelin notebooks)**: Interactive, real-time processing and analytics.
- **Amazon Kinesis Data Firehose**: Buffering and formatting processed data (configured with 30 seconds or 5 MB buffering).
- **Amazon S3**: Durable storage of data.
- **AWS Glue**: Serverless data integration service for automated data cataloging.
- **Amazon Athena**: Interactive queries against S3 data.
- **Amazon QuickSight**: Data visualization and analytics dashboards.

## Detailed Workflow

### 1. Data Generation & Ingestion
- Use the Kinesis Data Generator to simulate real-time streaming data, mimicking scenarios like gaming servers or mobile devices.
- Stream data directly into the `data2dashboard` Kinesis Data Stream.

  <img width="1021" alt="Screenshot 2025-03-14 at 10 07 17 AM" src="https://github.com/user-attachments/assets/294c4245-3bbf-4cc1-b8ec-49ee72391403" />
![lab1arch](https://github.com/user-attachments/assets/598a0bc1-e805-49fc-a26d-73366e943fc2)


### 2. Real-time Data Processing
- Deploy Amazon Managed Apache Flink via Studio Notebooks (Apache Zeppelin).
- Execute SQL scripts to create and manage real-time data streams and tables.
- Analyze real-time data streams (e.g., player kill ratios, team performance metrics).

<img width="1136" alt="Screenshot 2025-03-12 at 10 50 45 AM" src="https://github.com/user-attachments/assets/b462b198-75a2-471d-b313-9a04e06da014" />
  

### 3. Data Delivery and Storage
- Deliver processed data using Amazon Kinesis Data Firehose.
- Configure buffering (30-second intervals or 5 MB threshold) and GZIP compression.
- Store data in structured paths in Amazon S3.

### 4. Data Cataloging & Querying
- Use AWS Glue crawlers to catalog data stored in Amazon S3.
- Query processed data via Amazon Athena, leveraging SQL queries.

### 5. Dashboard Creation & Visualization
- Connect Amazon QuickSight with Amazon Athena as a data source.
- Build dynamic visualizations, such as line charts (player kill ratios) and bar graphs (player deaths).
- Create interactive dashboards for monitoring real-time analytics and performance.
<img width="1467" alt="Screenshot 2025-03-13 at 9 10 16 PM" src="https://github.com/user-attachments/assets/628a3d9f-a35e-459e-8377-ab43f696d664" />
<img width="1470" alt="Screenshot 2025-03-13 at 9 11 02 PM" src="https://github.com/user-attachments/assets/49bbf8c8-30c4-4b4b-b939-984c016a0b95" />

  

## Setup & Usage

### Prerequisites
- AWS Account with required permissions (Region: us-east-1 recommended).
- AWS CLI installed and configured.

### Quick Setup Steps
1. Configure Kinesis Data Generator to simulate data.
2. Create Apache Flink Studio Notebook in AWS Console to process incoming data.
3. Set up Amazon Kinesis Data Firehose for buffering and delivery to Amazon S3.
4. Catalog data using AWS Glue and query data with Amazon Athena.
5. Visualize data through Amazon QuickSight dashboards.

## Use Cases
- Real-time analytics for gaming (leaderboards, recommendations).
- Operational monitoring and insights.
- Interactive data exploration and analysis.


