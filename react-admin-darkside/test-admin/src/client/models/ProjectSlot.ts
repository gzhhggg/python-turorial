/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type ProjectSlot = {
    /**
     * プロジェクトID
     */
    project_id: number;
    name: string;
    /**
     * 募集開始日
     */
    start_date: string;
    /**
     * 募集終了日
     */
    end_date?: (string | null);
    /**
     * 予算
     */
    budget: number;
    id: number;
    created_at: string;
    deleted_at: (string | null);
};

