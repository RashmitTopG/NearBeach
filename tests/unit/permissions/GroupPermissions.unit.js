// Vitest
import { describe, expect, test } from "vitest";
import {mount, VueWrapper} from "@vue/test-utils";

// Import vue component
import GroupPermissions from "/src/js/components/permissions/GroupPermissions.vue";

// VueX
import { store } from "/src/js/vuex-store";

// Axios
const axios = require("axios");

describe(' ParentModules.vue - rendering component', () => {
    //Using mount - insert data
    const wrapper = mount(GroupPermissions, {
        props: {},
        global: {
            plugins: [store],
            mocks: {
                axios,
            }
        },
    });

    test('Empty test', () => {
    });
})
