<script>
  import { onMount } from "svelte";

  export let id;
  export let content;
  export let close_function;
  export let repeat_function;

  let MuscleGroups = "";
  let MuscleGroupsShort = "";
  let Equipment = "";
  let Difficulty = "";
  let Type = "";

  function GetText(input) {
    let output = "";
    for (let i = 0; i < input.length; i++) {
      output = output + input[i] + ", ";
    }
    output = output.substring(0, output.length - 2);
    return output;
  }
  function GetTextShort(input, maxlength = 28) {
    let output = GetText(input);

    output =
      output.length <= maxlength ? output : output.substr(0, maxlength) + "...";
    return output;
  }
</script>

<a
  class="btn btn-outline-secondary col-8 text-left textSpecial"
  data-bs-toggle="collapse"
  href="#collapseLink{id}"
  role="button"
  aria-expanded="false"
  aria-controls="collapseExample"
>
  {GetTextShort(content.MuscleGroups)}
</a>
<button
  class="btn bi-arrow-repeat col"
  type="button"
  style="font-size:130%"
  on:click={repeat_function(id)}
/>
<button
  class="btn btn-close col-1"
  type="button"
  on:click={close_function(id)}
/>

<div class="collapse" id="collapseLink{id}">
  <div class="card card-body bg-transparent cardSpecial">
    <b> Muscle groups:</b>
    <p>{GetText(content.MuscleGroups)}</p>
    <b> Equipment:</b>
    <p>{GetText(content.Equipments)}</p>
    <b> Difficulty:</b>
    <p>{GetText(content.Experience)}</p>
    <b> Exercise Type:</b>
    <p>{GetText(content.ExerciseTypes)}</p>
  </div>
</div>

<style>
  .cardSpecial {
    border: 0 !important;
    padding-bottom: 0 !important;
    padding-top: 10px;
  }
  .cardSpecial > p {
    margin: 0;
  }
  .textSpecial {
    text-align: left;
  }
</style>
