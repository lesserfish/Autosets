<script>
    import { onMount } from "svelte";
    import * as WorkoutJSON  from "../Database/db.json"
    export let AppObjects = {
        workoutObject : [],
        muscleGroupArray : [],
        exerciseTypeArray : [],
        equipmentArray : [],
        experienceArray : [],
    };


    onMount(async () => {
        
        AppObjects.workoutObject = WorkoutJSON.Exercises;
		AppObjects.muscleGroupArray = WorkoutJSON.MuscleGroups;
		AppObjects.exerciseTypeArray = WorkoutJSON.Types;
		AppObjects.equipmentArray = WorkoutJSON.Equipment;
		AppObjects.experienceArray = WorkoutJSON.Experience;
    });
</script>
