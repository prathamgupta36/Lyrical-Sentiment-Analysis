import { useContext, useRef } from "react";
import StateContext from "../../store/state-context";

import css from "./DeepLearning.module.css";
import BarChart from "../ui/BarChart";

function DeepLearning() {
	const stateContext = useContext(StateContext); 
	
	return (
		<div>
			<div className={css.title}>Deep Learning Model Results</div>
			<br />
			<BarChart results={stateContext.results}/>
		</div>
	);
}

export default DeepLearning;