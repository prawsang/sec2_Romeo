import { SET_CURRENT_EQUIPMENT, 
    SET_CURRENT_STYLES, 
    SET_CURRENT_AVAILTIMES,
    SET_FIELD_ERRORS
} from "common/action-types";

const initialState = {
    currentEquipment: [],
    currentStyles: [],
    currentAvailTime: [],
    fieldErrors: false
};

export default (state = initialState, action) => {
	const { type, payload } = action;

	switch (type) {
		case SET_CURRENT_EQUIPMENT:
			return {
				...state,
				currentEquipment: payload.currentEquipment
            };
        case SET_CURRENT_STYLES:
            return {
                ...state,
                currentStyles: payload.currentStyles
            };
        case SET_CURRENT_AVAILTIMES:
            return {
                ...state,
                currentAvailTime: payload.currentAvailTime
            }
        case SET_FIELD_ERRORS:
            return {
                ...state,
                fieldErrors: payload.errors
            }
		default: return state;
	}
};
