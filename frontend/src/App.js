import './App.css';

import { useEffect, useState } from 'react';

import axios from 'axios';


function App() {

  const [records, setRecords] = useState([]);

  const [file, setFile] = useState(null);


  useEffect(() => {

    fetchRecords();

  }, []);


  const fetchRecords = async () => {

    const response = await axios.get(
      'https://breathe-esg-assignment-05jx.onrender.com/api/review/'
    );

    setRecords(response.data);
  };


  const handleFileChange = (event) => {

    setFile(event.target.files[0]);
  };


  const uploadFile = async () => {

    if (!file) {

      alert('Please select a CSV file');

      return;
    }

    const formData = new FormData();

    formData.append('file', file);

    await axios.post(
      'https://breathe-esg-assignment-05jx.onrender.com/api/upload/sap/',
      formData
    );

    alert('File uploaded successfully');

    fetchRecords();
  };


  const approveRecord = async (id) => {

    await axios.post(
      `https://breathe-esg-assignment-05jx.onrender.com/api/review/${id}/approve/`
    );

    fetchRecords();
  };


  const lockRecord = async (id) => {

    await axios.post(
      `https://breathe-esg-assignment-05jx.onrender.com/api/review/${id}/lock/`
    );

    fetchRecords();
  };


  return (

    <div className="App">

      <div className="dashboard-container">

      <h1>Breathe ESG Dashboard</h1>


      <div className="upload-section">

        <input
          type="file"
          onChange={handleFileChange}
        />

        <button onClick={uploadFile}>
          Upload CSV
        </button>

      </div>


      <table>

        <thead>

          <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>Scope</th>
            <th>Status</th>
            <th>Suspicious</th>
            <th>Actions</th>
          </tr>

        </thead>

        <tbody>

          {records.map((record) => (

            <tr key={record.id}>

              <td>{record.id}</td>

              <td>{record.category}</td>

              <td>{record.quantity}</td>

              <td>{record.normalized_unit}</td>

              <td>{record.scope}</td>

              <td>

                <span className={`status ${record.review_status}`}>
                  {record.review_status}
                </span>

              </td>
              <td>
                {record.suspicious_flag ? '⚠️ Yes' : 'No'}
              </td>

              <td>

                {!record.locked_for_audit && (

      <>
  
            <button
            onClick={() => approveRecord(record.id)}
            >
            Approve
            </button>

            <button
            onClick={() => lockRecord(record.id)}
            >
            Lock
            </button>

      </>

        )}

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
    </div>
  );
}

export default App;