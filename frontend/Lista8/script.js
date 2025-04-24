const pokemonListElement = document.getElementById("pokemonList");
const errorText = document.getElementById("errorText");
const pokemonDetailsElement = document.getElementById("pokemonDetails");
const pokemonNameElement = document.getElementById("pokemonName");
const pokemonImageElement = document.getElementById("pokemonImg");
const pokemonTypeElement = document.getElementById("pokemonTypes");
const pokemonStatsElement = document.getElementById("pokemonStats");
const pokemonFlavorTextElement = document.getElementById("pokemonFlavorText");
const loading = document.getElementById("loading");


pokemonListElement.innerHTML = "";
pokemonDetailsElement.style.display = "none";

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

async function preloadImage(src) {
  const img = new Image();
  img.src = src;
  await img.decode();
  return img;
}

async function fetchPokemonList() {
  loading.style.display = "block";
  pokemonListElement.innerHTML = "";
  try {
    const res = await fetch("https://pokeapi.co/api/v2/pokemon-species?limit=151");
    const data = await res.json();

    data.results.forEach((pokemon) => {
      const li = document.createElement("li");
      li.textContent = capitalize(pokemon.name);
      li.addEventListener("click", () => loadPokemon(pokemon.name));
      pokemonListElement.appendChild(li);
    });
  } catch (err) {
    console.error("Error loading Pokémon list:", err);
    errorText.style.display = "block";
  } finally {
    loading.style.display = "none";
  }
}

async function loadPokemon(pokemonName) {
  loading.style.display = "block";
  pokemonDetailsElement.style.display = "none";
  try {
    const species = await fetch(`https://pokeapi.co/api/v2/pokemon-species/${pokemonName}`);
    const speciesData = await species.json();

    const defaultVariety = speciesData.varieties.find(v => v.is_default);
    if (!defaultVariety) {
      throw new Error("No default variety found");
    }

    const pokemonUrl = defaultVariety.pokemon.url;

    const pokemonRes = await fetch(pokemonUrl);
    const pokemonData = await pokemonRes.json();

    await renderPokemonDetails(pokemonData, speciesData);
  }
  catch (err) {
    console.error("Error loading Pokémon details:", err);
    errorText.style.display = "block";
  }
  finally {
    loading.style.display = "none";
  }
}

async function renderPokemonDetails(pokemonData, speciesData) {
  pokemonNameElement.textContent = capitalize(pokemonData.name);

  const spriteUrl = pokemonData.sprites.front_default;
  await preloadImage(spriteUrl);
  pokemonImageElement.src = spriteUrl;
  pokemonImageElement.alt = pokemonData.name;
  pokemonImageElement.style.display = "block";

  pokemonTypeElement.innerHTML = "";
  pokemonData.types.forEach(type => {
    const span = document.createElement("span");
    span.className = "type";
    span.textContent = capitalize(type.type.name);
    pokemonTypeElement.appendChild(span);
  });

  pokemonStatsElement.innerHTML = "";
  pokemonData.stats.forEach(stat => {
    const statDiv = document.createElement("div");
    statDiv.className = "stat";

    const nameSpan = document.createElement("span");
    nameSpan.textContent = capitalize(stat.stat.name);

    const valueSpan = document.createElement("span");
    valueSpan.textContent = stat.base_stat;

    statDiv.appendChild(nameSpan);
    statDiv.appendChild(valueSpan);
    pokemonStatsElement.appendChild(statDiv);
  });

  const flavorText = speciesData.flavor_text_entries.find(entry => entry.language.name === "en");
  pokemonFlavorTextElement.textContent = flavorText ? flavorText.flavor_text.replace(/[\n\f]/g, " ") : "No flavor text available.";
  pokemonFlavorTextElement.style.display = "block";

  pokemonDetailsElement.style.display = "flex";
}

fetchPokemonList();