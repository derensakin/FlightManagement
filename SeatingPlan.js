// src/components/SeatingPlan.js
import React from 'react';

const SeatingPlan = ({ seatingPlan }) => {
  if (!seatingPlan) {
    return <div>No seating plan available</div>;
  }

  return (
    <div>
      <h3>Seating Plan</h3>
      <div className="seating-plan">
        {seatingPlan.map((row, rowIndex) => (
          <div key={rowIndex} className="seating-row">
            {row.map((seat, seatIndex) => (
              <div key={seatIndex} className="seat">
                {seat}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SeatingPlan;