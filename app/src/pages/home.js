import React from "react";
export default function Home(){
    return (

        <div className="Campus Choice">
            <header>Breakfast</header>
            <input type="radio" id="livi" name="campus" value="Livingston" />
            <label htmlFor="livi">Livingston</label><br />
            <input type="radio" id="busch" name="campus" value="Busch" />
            <label htmlFor="busch">Busch</label><br />
            <input type="radio" id="ca" name="campus" value="College Avenue" />
            <label htmlFor="ca">College Avenue</label><br />
            <input type="radio" id="cd" name="campus" value="Cook & Douglass" />
            <label htmlFor="cd">Cook & Douglass</label><br />
            <button>Submit</button>
        </div>
        
    )
}
