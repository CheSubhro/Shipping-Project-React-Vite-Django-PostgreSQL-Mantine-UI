Smart Logistics & Shipping Calculator
A professional full-stack web application that calculates real-time shipping costs based on actual road distance and package weight.

✨ Features
Smart Geocoding: Automatically converts city names into coordinates using Nominatim (OpenStreetMap).

Real Road Distance: Uses OSRM API to calculate driving distance instead of simple straight lines.

Dynamic Costing Engine: Calculates price based on a base fare + distance (per km) + weight (per kg).

Cloud Database: Stores all shipping records in Neon PostgreSQL.

Modern UI: Responsive and clean dashboard built with Mantine UI.

🛠️ Tech Stack
Frontend: React.js (Vite), Mantine UI, Axios.

Backend: Django, Django REST Framework.

Database: Neon PostgreSQL (Cloud).

External APIs: OpenStreetMap (Nominatim), OSRM Routing.

<img width="900" height="825" alt="localhost_5173_ (18)" src="https://github.com/user-attachments/assets/74fa223d-1129-472d-a37d-aa026168dab2" />
<img width="915" height="641" alt="127 0 0 1_8000_admin_shipping_shippingrate_" src="https://github.com/user-attachments/assets/c67494ca-a109-4f6f-9c0f-d5dd06f96576" />


🚀 Getting Started
1. Prerequisites
Python 3.x

Node.js & npm

2. Backend Setup
Navigate to the backend folder:

Bash
cd backend
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/Scripts/activate  # For Windows
Install dependencies:

Bash
pip install -r requirements.txt
Run migrations:

Bash
python manage.py migrate
Start the server:

Bash
python manage.py runserver
3. Frontend Setup
Navigate to the frontend folder:

Bash
cd frontend
Install dependencies:

Bash
npm install
Start the development server:

Bash
npm run dev
⚙️ API Configuration
The backend calculates shipping rates via the following endpoint:

URL: http://127.0.0.1:8000/api/shipping/calculate/

Method: POST

Payload:

JSON
{
  "source_city": "Kolkata",
  "destination_city": "Delhi",
  "weight_kg": 5
}
