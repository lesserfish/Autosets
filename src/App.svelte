<script>
import Introduction from "./Componenta/Introduction.svelte"
import Template from "./Componenta/Template.svelte"
import Output from "./Componenta/Output.svelte"

let mode = 0;
let value = 0;

</script>

<div>
	<div class="Header"></div>

	<button on:click={() => { mode = Math.max(mode - 1, 0)}}> Previous Step </button> 
	<button on:click={() => { mode = Math.min(mode + 1, 2)}}> Next Step</button> 

	<div class="Main">
		{#if mode == 0}
			<Introduction />
		{:else if mode == 1}
			<Template bind:value={value}/>
		{:else}
			<Output bind:value={value}/>
		{/if}	
	</div>

	<div class="Footer"></div>
</div>

<style>
</style>