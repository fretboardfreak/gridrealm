// rollup config

// use node resolve to find dependencies in "./node_modules"
import resolve from 'rollup-plugin-node-resolve';
import babel from 'rollup-plugin-babel';
import commonjs from 'rollup-plugin-commonjs';
import inject from 'rollup-plugin-inject';

export default {
  input: 'src/client/js/gridrealm.js',
  output: {
    file: 'dist/client/js/gridrealm.js',
    format: 'iife'
  },
  external: ['bootstrap', 'jquery'],
  plugins: [
    resolve(),
    babel({
      exclude: 'node_modules/**' // only transpile our source code
    }),
    commonjs(),
    inject({
      include: '**/*.js',
      exclude: 'node_modules/**',
      jQuery: 'jquery',
      $: 'jquery',
    })
  ]
};
