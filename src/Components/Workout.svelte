<script>
  export let Name;
  export let Description;
  export let URL;
  export let Image;
  export let MuscleGroup;
  export let ExerciseType;
  export let Equipment;
  export let Experience;
</script>

<div class="workout-instance">
  <div class="exercise*name">
    <p>
      {Name}
    </p>
  </div>
  <div class="exercise-description">
    <p>
      {Description}
    </p>
  </div>
  <div class="exercise-url">
    <p>
      {URL}
    </p>
  </div>
  <div class="exercise-image">
    <p>
      {Image}
    </p>
  </div>
  <div class="exercise-musclegroup">
    <p>
      {MuscleGroup}
    </p>
  </div>
  <div class="exercise-type">
    <p>
      {ExerciseType}
    </p>
  </div>
  <div class="exercise-equipment">
    <p>
      {Equipment}
    </p>
  </div>
  <div class="exercise-experience">
    <p>
      {Experience}
    </p>
  </div>
</div>
